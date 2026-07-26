import streamlit as st
import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo

# -------------------------------------------------------------------
# CONFIGURACIÓN Y PERSISTENCIA
# -------------------------------------------------------------------
st.set_page_config(page_title="ACF", page_icon="💳", layout="centered")

ARCHIVO_BD = "datos.json"

DATOS_INICIALES = {
    "semana_actual": datetime.now(ZoneInfo("Europe/Madrid")).isocalendar()[1],
    "sugerencias": [],
    "usuarios": {
        "eric": {
            "password": "2020_Electronica",
            "creditos": 100,
            "historial": [],
            "logros": [],
            "stock_usado": {},
            "amigos": [],
            "solicitudes_recibidas": []
        }
    }
}

CATALOGO_GASTAR = [
    {"id": 1, "emoji": "🛋️", "nombre": "Librarte de una tarea por 1 día", "coste": 60, "limite_diario": 1},
    {"id": 2, "emoji": "📺", "nombre": "Ver la tele (1h)", "coste": 15, "limite_diario": 3},
    {"id": 3, "emoji": "🃏", "nombre": "Cambiar de juego/regla", "coste": 30, "limite_diario": 2},
    {"id": 4, "emoji": "🍫", "nombre": "Comer dulce", "coste": 15, "limite_diario": 1},
    {"id": 5, "emoji": "🎯", "nombre": "Elegir el primer turno", "coste": 10, "limite_diario": 1},
    {"id": 6, "emoji": "🎵", "nombre": "Elegir musica (1h)", "coste": 10, "limite_diario": 2},
    {"id": 7, "emoji": "🧊", "nombre": "Camarero por un momento", "coste": 20, "limite_diario": 1},
    {"id": 8, "emoji": "🍕", "nombre": "El ingrediente prohibido", "coste": 20, "limite_diario": 1},
    {"id": 9, "emoji": "💆", "nombre": "Masaje 5-10 min", "coste": 10, "limite_diario": 1}
]

CATALOGO_GANAR = [
    {"id": 101, "emoji": "🧺", "nombre": "Recoger el tendedero", "recompensa": 15, "limite_diario": 2},
    {"id": 102, "emoji": "🧹", "nombre": "Recoger habitación", "recompensa": 20, "limite_diario": 1},
    {"id": 103, "emoji": "🍽️", "nombre": "Lavar los platos", "recompensa": 15, "limite_diario": 3},
    {"id": 104, "emoji": "🍽️", "nombre": "Poner / Quitar la mesa", "recompensa": 10, "limite_diario": 2},
    {"id": 105, "emoji": "🗑️", "nombre": "Sacar la basura", "recompensa": 10, "limite_diario": 1},
    {"id": 106, "emoji": "🍽️", "nombre": "Recoger el lavavajillas", "recompensa": 3, "limite_diario": 1},
    {"id": 107, "emoji": "👕", "nombre": "Poner el tendedero", "recompensa": 15, "limite_diario": 2},
    {"id": 108, "emoji": "🪴", "nombre": "Regar las plantas", "recompensa": 10, "limite_diario": 1},
    {"id": 109, "emoji": "👔", "nombre": "Doblar la ropa del tendedero", "recompensa": 5, "limite_diario": 2}
]

def obtener_fecha_hora():
    """Devuelve la fecha y hora formateada según la zona horaria de Madrid"""
    return datetime.now(ZoneInfo("Europe/Madrid")).strftime("%d/%m/%Y %H:%M")

def cargar_datos():
    if not os.path.exists(ARCHIVO_BD):
        guardar_datos(DATOS_INICIALES)
        return DATOS_INICIALES
    try:
        with open(ARCHIVO_BD, "r", encoding="utf-8") as f:
            datos = json.load(f)
        
        datos.setdefault("sugerencias", [])
        
        semana_hoy = datetime.now(ZoneInfo("Europe/Madrid")).isocalendar()[1]
        if datos.get("semana_actual") != semana_hoy:
            datos["semana_actual"] = semana_hoy
            f_act = obtener_fecha_hora()
            for usr, d in datos["usuarios"].items():
                if d.get("creditos", 0) < 100:
                    d["creditos"] = 100
                d["stock_usado"] = {}
                d["historial"].append({"actividad": "🔄 Reinicio semanal de límites", "coste": 0, "fecha": f_act})
            guardar_datos(datos)
        return datos
    except Exception:
        return DATOS_INICIALES

def guardar_datos(datos):
    with open(ARCHIVO_BD, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

# -------------------------------------------------------------------
# GESTIÓN DE SESIÓN Y LOGIN
# -------------------------------------------------------------------
if "usuario" not in st.session_state:
    st.session_state.usuario = None

if not st.session_state.usuario:
    db = cargar_datos()
    st.title("🔑 ACF — Acceso")
    
    tab_login, tab_reg = st.tabs(["Iniciar Sesión", "Registrarse"])
    
    with tab_login:
        user_in = st.text_input("Usuario", key="l_user").strip().lower()
        pass_in = st.text_input("Contraseña", type="password", key="l_pass")
        if st.button("Entrar ➔", type="primary", use_container_width=True):
            if user_in in db["usuarios"] and db["usuarios"][user_in]["password"] == pass_in:
                st.session_state.usuario = user_in
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")

    with tab_reg:
        r_user = st.text_input("Nuevo Usuario", key="r_user").strip().lower()
        r_pass = st.text_input("Contraseña", type="password", key="r_pass")
        if st.button("Crear cuenta ✨", use_container_width=True):
            if not r_user or not r_pass:
                st.warning("Rellena todos los campos")
            elif r_user in db["usuarios"]:
                st.error("El usuario ya existe")
            else:
                db["usuarios"][r_user] = {
                    "password": r_pass,
                    "creditos": 100,
                    "historial": [],
                    "logros": [],
                    "stock_usado": {},
                    "amigos": [],
                    "solicitudes_recibidas": []
                }
                guardar_datos(db)
                st.success("¡Cuenta creada! Ya puedes iniciar sesión.")
    st.stop()

# -------------------------------------------------------------------
# PANEL PRINCIPAL EN TIEMPO REAL
# -------------------------------------------------------------------
@st.fragment(run_every=3)
def renderizar_panel_principal():
    db = cargar_datos()
    usr = st.session_state.usuario

    if usr not in db["usuarios"]:
        st.session_state.usuario = None
        st.rerun()

    usr_data = db["usuarios"][usr]

    col_head1, col_head2 = st.columns([3, 1])
    with col_head1:
        st.title(f"👤 {usr.capitalize()}")
    with col_head2:
        if st.button("Salir 🚪"):
            st.session_state.usuario = None
            st.rerun()

    st.metric(label="Saldo Disponible", value=f"{usr_data['creditos']} Créditos")

    tab_perfil, tab_ganar, tab_tienda, tab_comunidad = st.tabs(["Mi Perfil", "💪 Ganar", "🛒 Gastar", "👥 Comunidad"])

    # 1. PERFIL
    with tab_perfil:
        st.subheader("📜 Historial de Actividad")
        if not usr_data["historial"]:
            st.info("Sin movimientos recientes")
        else:
            for item in reversed(usr_data["historial"][-5:]):
                c = item["coste"]
                signo = f"-{c} cr" if c > 0 else (f"+{abs(c)} cr" if c < 0 else "0 cr")
                st.text(f"{item['fecha']} | {item['actividad']} ({signo})")

        st.divider()

        # SUGERENCIAS
        st.subheader("💡 Enviar una Sugerencia")
        st.caption("¿Tienes alguna idea para mejorar la app o sugerir tareas/premios?")
        
        sugerencia_txt = st.text_area("Escribe tu sugerencia aquí", key="input_sugerencia", placeholder="Ej: Añadir una recompensa para ir al cine...").strip()
        
        if st.button("Enviar Sugerencia 📩"):
            if sugerencia_txt:
                nueva_sug = {
                    "usuario": usr.capitalize(),
                    "texto": sugerencia_txt,
                    "fecha": obtener_fecha_hora()
                }
                db.setdefault("sugerencias", []).append(nueva_sug)
                guardar_datos(db)
                
                # Muestra mensaje de éxito y vacía el campo de texto
                st.toast("✅ Sugerencia enviada correctamente. ¡Muchas gracias!", icon="🎉")
                st.session_state["input_sugerencia"] = ""
                st.rerun()
            else:
                st.warning("Por favor, escribe algo antes de enviar.")

        # VISTA EXCLUSIVA DE SUGERENCIAS PARA ERIC
        if usr == "eric":
            st.divider()
            col_sug_head1, col_sug_head2 = st.columns([3, 1])
            with col_sug_head1:
                st.subheader("📥 Sugerencias Recibidas")
            with col_sug_head2:
                if db.get("sugerencias") and st.button("Vaciar todas 🗑️", key="btn_vaciar_sug"):
                    db["sugerencias"] = []
                    guardar_datos(db)
                    st.rerun()

            sugerencias_lista = db.get("sugerencias", [])
            
            if not sugerencias_lista:
                st.info("No hay sugerencias registradas por ahora.")
            else:
                for idx, sug in enumerate(list(sugerencias_lista)):
                    col_s1, col_s2 = st.columns([4, 1])
                    with col_s1:
                        st.markdown(f"**👤 {sug['usuario']}** — *{sug['fecha']}*")
                        st.write(f"💬 \"{sug['texto']}\"")
                    with col_s2:
                        if st.button("Borrar ❌", key=f"del_sug_{idx}"):
                            db["sugerencias"].remove(sug)
                            guardar_datos(db)
                            st.rerun()
                    st.divider()

    # 2. GANAR CRÉDITOS
    with tab_ganar:
        st.subheader("Completa tareas para ganar créditos")
        
        # BUSCADOR
        search_ganar = st.text_input("🔍 Buscar tarea...", key="search_ganar").strip().lower()
        
        fecha_hoy = datetime.now(ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d")
        stock = usr_data.setdefault("stock_usado", {}).setdefault(fecha_hoy, {})

        # Filtrar por texto
        tareas_filtradas = [t for t in CATALOGO_GANAR if search_ganar in t["nombre"].lower()]

        if not tareas_filtradas:
            st.info("No se encontraron tareas con esa búsqueda.")
        else:
            for item in tareas_filtradas:
                usados = stock.get(str(item["id"]), 0)
                disp = item["limite_diario"] - usados
                
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"**{item['emoji']} {item['nombre']}** \n`+{item['recompensa']} cr` | Disponibles: {disp}/{item['limite_diario']}")
                with c2:
                    if st.button("Completar", key=f"ganar_{item['id']}", disabled=(disp <= 0)):
                        usr_data["creditos"] += item["recompensa"]
                        stock[str(item["id"])] = usados + 1
                        usr_data["historial"].append({
                            "actividad": f"{item['emoji']} {item['nombre']}", 
                            "coste": -item["recompensa"], 
                            "fecha": obtener_fecha_hora()
                        })
                        guardar_datos(db)
                        st.toast(f"¡+{item['recompensa']} créditos obtenidos!", icon="💰")
                        st.rerun()
                st.divider()

    # 3. GASTAR CRÉDITOS
    with tab_tienda:
        st.subheader("Canjea tus créditos por recompensas")
        
        # BUSCADOR
        search_gastar = st.text_input("🔍 Buscar recompensa...", key="search_gastar").strip().lower()
        
        fecha_hoy = datetime.now(ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d")
        stock = usr_data.setdefault("stock_usado", {}).setdefault(fecha_hoy, {})

        # Filtrar por texto
        recompensas_filtradas = [r for r in CATALOGO_GASTAR if search_gastar in r["nombre"].lower()]

        if not recompensas_filtradas:
            st.info("No se encontraron recompensas con esa búsqueda.")
        else:
            for item in recompensas_filtradas:
                usados = stock.get(str(item["id"]), 0)
                disp = item["limite_diario"] - usados
                
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"**{item['emoji']} {item['nombre']}** \n`Coste: {item['coste']} cr` | Disponibles: {disp}/{item['limite_diario']}")
                with c2:
                    puedes_comprar = disp > 0 and usr_data["creditos"] >= item["coste"]
                    if st.button("Canjear", key=f"gastar_{item['id']}", disabled=not puedes_comprar):
                        usr_data["creditos"] -= item["coste"]
                        stock[str(item["id"])] = usados + 1
                        usr_data["historial"].append({
                            "actividad": f"{item['emoji']} {item['nombre']}", 
                            "coste": item["coste"], 
                            "fecha": obtener_fecha_hora()
                        })
                        guardar_datos(db)
                        st.balloons()
                        st.toast(f"¡Canjeado: {item['nombre']}!", icon="🎉")
                        st.rerun()
                st.divider()

    # 4. COMUNIDAD
    with tab_comunidad:
        st.subheader("📩 Enviar Solicitud de Amistad")
        nuevo_amigo = st.text_input("Usuario a añadir", key="add_amigo").strip().lower()
        if st.button("Enviar Solicitud"):
            if nuevo_amigo and nuevo_amigo in db["usuarios"] and nuevo_amigo != usr:
                dest = db["usuarios"][nuevo_amigo]
                solis = dest.setdefault("solicitudes_recibidas", [])
                if usr not in solis and usr not in dest.get("amigos", []):
                    solis.append(usr)
                    guardar_datos(db)
                    st.success(f"Solicitud enviada a {nuevo_amigo.capitalize()}")
                else:
                    st.info("Ya existe una solicitud o ya son amigos")
            else:
                st.error("Usuario no válido")

        solis = usr_data.get("solicitudes_recibidas", [])
        if solis:
            st.subheader("📬 Solicitudes Pendientes")
            for s in solis:
                c1, c2, c3 = st.columns([2, 1, 1])
                c1.write(f"👤 **{s.capitalize()}**")
                if c2.button("Aceptar ✅", key=f"ac_{s}"):
                    usr_data["solicitudes_recibidas"].remove(s)
                    usr_data.setdefault("amigos", []).append(s)
                    db["usuarios"][s].setdefault("amigos", []).append(usr)
                    guardar_datos(db)
                    st.rerun()
                if c3.button("Rechazar ❌", key=f"rec_{s}"):
                    usr_data["solicitudes_recibidas"].remove(s)
                    guardar_datos(db)
                    st.rerun()

        st.subheader("👥 Tu Comunidad")
        amigos = usr_data.get("amigos", [])
        if not amigos:
            st.info("Aún no tienes miembros en tu comunidad.")
        else:
            for a in amigos:
                data_a = db["usuarios"].get(a, {})
                with st.expander(f"👤 {a.capitalize()} — Saldo: {data_a.get('creditos', 0)} cr"):
                    max_tr = max(1, usr_data["creditos"])
                    monto = st.number_input(f"Transferir créditos a {a.capitalize()}", min_value=1, max_value=max_tr, key=f"tr_{a}")
                    if st.button(f"Enviar a {a.capitalize()}", key=f"btn_tr_{a}"):
                        if usr_data["creditos"] >= monto:
                            usr_data["creditos"] -= monto
                            data_a["creditos"] += monto
                            f_act = obtener_fecha_hora()
                            usr_data["historial"].append({"actividad": f"💸 Envío a {a.capitalize()}", "coste": monto, "fecha": f_act})
                            data_a["historial"].append({"actividad": f"🎁 Recibido de {usr.capitalize()}", "coste": -monto, "fecha": f_act})
                            guardar_datos(db)
                            st.success(f"¡Enviados {monto} créditos!")
                            st.rerun()
                        else:
                            st.error("No tienes suficientes créditos")

                    st.markdown("**Última actividad:**")
                    for h in reversed(data_a.get("historial", [])[-3:]):
                        st.caption(f"{h['fecha']} - {h['actividad']}")

# Ejecución
renderizar_panel_principal()
