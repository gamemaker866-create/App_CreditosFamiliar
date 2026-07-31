import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
from supabase import create_client
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="ACF", page_icon="💳", layout="centered")

st_autorefresh(interval=5000, key="datarefresh")

SUPABASE_URL = "https://rhejicyuvtfymnmjlpky.supabase.co" # Tu URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJoZWppY3l1dnRmeW1ubWpscGt5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODUwODY2MDMsImV4cCI6MjEwMDY2MjYwM30.DUAOn7PdHC7x_GyIAMCfbmIkEk7eZymFnIMsSnL3h6Q"

@st.cache_resource
def init_supabase():
    # 🧹 LIMPIEZA AUTOMÁTICA DE LA URL:
    url_limpia = SUPABASE_URL.strip().rstrip("/")
    if url_limpia.endswith("/rest/v1"):
        url_limpia = url_limpia[:-8]
        
    return create_client(url_limpia, SUPABASE_KEY)

supabase = init_supabase()

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
    {"id": 1, "emoji": "🛋️", "nombre": "Librarte de una tarea por 1 día", "coste": 30, "limite_diario": 1},
    {"id": 2, "emoji": "📺", "nombre": "Ver la tele (1h)", "coste": 15, "limite_diario": 2},
    {"id": 3, "emoji": "🃏", "nombre": "Cambiar de juego/regla", "coste": 30, "limite_diario": 2},
    {"id": 4, "emoji": "🍫", "nombre": "Comer dulce", "coste": 5, "limite_diario": 2},
    {"id": 5, "emoji": "🎯", "nombre": "Elegir el primer turno", "coste": 10, "limite_diario": 1},
    {"id": 6, "emoji": "🎵", "nombre": "Elegir musica (1h)", "coste": 10, "limite_diario": 2},
    {"id": 7, "emoji": "🧊", "nombre": "Camarero por un momento", "coste": 20, "limite_diario": 1},
    {"id": 8, "emoji": "🍕", "nombre": "El ingrediente prohibido", "coste": 20, "limite_diario": 1},
    {"id": 9, "emoji": "💆", "nombre": "Masaje 5-10 min", "coste": 10, "limite_diario": 1},
    {"id": 10, "emoji": "🛡️", "nombre": "Inmunidad en un juego", "coste": 20, "limite_diario": 1},
    {"id": 11, "emoji": "🎲", "nombre": "Elegir el juego de mesa de hoy", "coste": 20, "limite_diario": 1},
    {"id": 12, "emoji": "🪞", "nombre": "Carta espejo: Rebotar un favor", "coste": 25, "limite_diario": 1},
    {"id": 13, "emoji": "🤏", "nombre": "Impuesto del 10% de snack", "coste": 10, "limite_diario": 2},
    {"id": 14, "emoji": "🏆", "nombre": "Pase VIP: Fin de semana libre", "coste": 280, "limite_diario": 1, "destacado": True},
    {"id": 15, "emoji": "📜", "nombre": "Crear una regla absurda (1h)", "coste": 15, "limite_diario": 1},
    {"id": 16, "emoji": "⚖️", "nombre": "Voto de calidad en empates", "coste": 30, "limite_diario": 1},
    {"id": 17, "emoji": "🛋️", "nombre": "Reclamar la mejor manta/cojín", "coste": 10, "limite_diario": 1},
    {"id": 18, "emoji": "🤐", "nombre": "Palabra prohibida (1h)", "coste": 10, "limite_diario": 1},
    {"id": 19, "emoji": "🍕", "nombre": "Reclamar la última porción", "coste": 30, "limite_diario": 1},
    {"id": 20, "emoji": "🗑️", "nombre": "Inmunidad de basura (3 días)", "coste": 60, "limite_diario": 1},
    {"id": 21, "emoji": "🙏", "nombre": "Favor obligatorio", "coste": 20, "limite_diario": 1},
    {"id": 22, "emoji": "🥪", "nombre": "¡Sin corteza porfavor!", "coste": 15, "limite_diario": 1},
    {"id": 23, "emoji": "😴", "nombre": "Siesta (1h max.)", "coste": 5, "limite_diario": 1},
    {"id": 24, "emoji": "🎙️", "nombre": "Narración deportiva de tu vida (2 min)", "coste": 20, "limite_diario": 1},
    {"id": 25, "emoji": "👤", "nombre": "Hablar en tercera persona (1h)", "coste": 1, "limite_diario": 2},
    {"id": 26, "emoji": "🤫", "nombre": "Susurrar frases cotidianas (1h)", "coste": 2, "limite_diario": 2},
    {"id": 27, "emoji": "🕵️‍♂️", "nombre": "Cerrar frases con 'es un misterio'", "coste": 1, "limite_diario": 2},
    {"id": 28, "emoji": "🧊", "nombre": "Saludar a los electrodomésticos (24h)", "coste": 2, "limite_diario": 2},
    {"id": 29, "emoji": "🎬", "nombre": "Mirada a la cámara invisible (24h cada vez que pase algo gracioso o raro)", "coste": 2, "limite_diario": 3},
    {"id": 30, "emoji": "❓", "nombre": "Formular preguntas en modo concurso", "coste": 2, "limite_diario": 1}
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
    {"id": 109, "emoji": "👔", "nombre": "Doblar la ropa del tendedero", "recompensa": 5, "limite_diario": 2},
    {"id": 110, "emoji": "🫧", "nombre": "Poner la lavadora", "recompensa": 10, "limite_diario": 2},
    {"id": 111, "emoji": "🛍️", "nombre": "Ir a comprar (en el barrio)", "recompensa": 5, "limite_diario": 1},
    {"id": 112, "emoji": "🏃‍➡️", "nombre": "Hacer deporte", "recompensa": 10, "limite_diario": 2},
    {"id": 113, "emoji": "📖", "nombre": "Lectura de libro (30 min)", "recompensa": 10, "limite_diario": 3},
    {"id": 114, "emoji": "📚", "nombre": "Despolvar estantería o librería", "recompensa": 20, "limite_diario": 1},
    {"id": 115, "emoji": "🔋", "nombre": "Gestionar reciclaje de pilas/electrónicos", "recompensa": 15, "limite_diario": 1},
    {"id": 116, "emoji": "♻️", "nombre": "Manualidad con envase reciclado", "recompensa": 20, "limite_diario": 1},
    {"id": 117, "emoji": "📖", "nombre": "Logro: 14 días seguidos de lectura (30 min)", "recompensa": 40, "limite_diario": 1, "destacado": True}
]

def obtener_fecha_hora():
    return datetime.now(ZoneInfo("Europe/Madrid")).strftime("%d/%m/%Y %H:%M")

def esta_bloqueado(usr_data):
    bloqueado_hasta_str = usr_data.get("bloqueado_hasta")
    if not bloqueado_hasta_str:
        return False, None
    try:
        f_bloqueo = datetime.fromisoformat(bloqueado_hasta_str)
        ahora = datetime.now(ZoneInfo("Europe/Madrid"))
        if ahora < f_bloqueo:
            return True, f_bloqueo.strftime("%d/%m/%Y a las %H:%M")
        else:
            return False, None
    except Exception:
        return False, None

def cargar_datos():
    try:
        response = supabase.table("estado_app").select("datos").eq("id", 1).execute()
        if response.data and len(response.data) > 0 and response.data[0].get("datos"):
            datos = response.data[0]["datos"]
            
            datos.setdefault("sugerencias", [])
            datos.setdefault("reto_flash", None)
            datos.setdefault("subasta_activa", None)
            datos.setdefault("usuarios", {})
            datos.setdefault("catalogo_gastar", CATALOGO_GASTAR)
            datos.setdefault("catalogo_ganar", CATALOGO_GANAR)
            
            if not datos["usuarios"]:
                datos = DATOS_INICIALES
                guardar_datos(datos)

            for u_nombre, u_data in datos["usuarios"].items():
                u_data["amigos"] = list(dict.fromkeys(u_data.get("amigos", [])))
                u_data["solicitudes_recibidas"] = list(dict.fromkeys(u_data.get("solicitudes_recibidas", [])))
                u_data.setdefault("bloqueado_hasta", None)

            semana_hoy = datetime.now(ZoneInfo("Europe/Madrid")).isocalendar()[1]
            if datos.get("semana_actual") != semana_hoy:
                datos["semana_actual"] = semana_hoy
                f_act = obtener_fecha_hora()
                for usr, d in datos["usuarios"].items():
                    if d.get("creditos", 0) < 100:
                        d["creditos"] = 100
                    d["stock_usado"] = {}
                    d.setdefault("historial", []).append({"actividad": "🔄 Reinicio semanal de límites", "coste": 0, "fecha": f_act})
                guardar_datos(datos)
            return datos
        else:
            guardar_datos(DATOS_INICIALES)
            return DATOS_INICIALES
    except Exception as e:
        st.error(f"Error cargando datos de Supabase: {e}")
        return DATOS_INICIALES

def guardar_datos(datos):
    try:
        supabase.table("estado_app").upsert({"id": 1, "datos": datos}).execute()
    except Exception as e:
        st.error(f"Error guardando datos en Supabase: {e}")

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
                    "solicitudes_recibidas": [],
                    "bloqueado_hasta": None
                }
                guardar_datos(db)
                st.success("¡Cuenta creada! Ya puedes iniciar sesión.")
    st.stop()

# -------------------------------------------------------------------
# PANEL PRINCIPAL
# -------------------------------------------------------------------
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

    # Banner Reto Flash
    reto_actual = db.get("reto_flash")
    if reto_actual and reto_actual.get("activo"):
        st.info(f"🎯 **RETO FLASH DEL DÍA:** {reto_actual['texto']} \n\n *(Recompensa especial: +{reto_actual['recompensa']} cr)*")

    # Banner Subasta Activa
    subasta = db.get("subasta_activa")
    if subasta and subasta.get("activa"):
        with st.container(border=True):
            st.subheader(f"🔨 Subasta Activa: {subasta['item']}")
            if subasta['max_postor']:
                st.markdown(f"🏆 **Mayor puja actual:** `{subasta['puja_actual']} cr` por **{subasta['max_postor'].capitalize()}**")
            else:
                st.markdown(f"💰 **Puja de salida:** `{subasta['puja_actual']} cr` (¡Nadie ha pujado aún!)")

            usuario_bloqueado_sub, _ = esta_bloqueado(usr_data)
            puja_minima = subasta['puja_actual'] + 1
            
            c_sub1, c_sub2 = st.columns([2, 1])
            with c_sub1:
                nueva_puja = st.number_input(
                    "Tu puja", 
                    min_value=puja_minima, 
                    max_value=max(puja_minima, usr_data["creditos"]), 
                    step=5,
                    key="input_puja_sub"
                )
            with c_sub2:
                st.write("") 
                st.write("")
                if st.button("Pujar 🔨", use_container_width=True, disabled=usuario_bloqueado_sub or usr_data["creditos"] < puja_minima):
                    subasta["puja_actual"] = int(nueva_puja)
                    subasta["max_postor"] = usr
                    guardar_datos(db)
                    st.toast(f"¡Has pujado {nueva_puja} cr!", icon="🔨")
                    st.rerun()

    usuario_bloqueado, fecha_fin_bloqueo = esta_bloqueado(usr_data)

    nombres_tabs = ["Mi Perfil", "💪 Ganar", "🛒 Gastar", "👥 Comunidad"]
    if usr == "eric":
        nombres_tabs.append("⚙️ Panel Admin")

    tabs = st.tabs(nombres_tabs)
    tab_perfil = tabs[0]
    tab_ganar = tabs[1]
    tab_tienda = tabs[2]
    tab_comunidad = tabs[3]
    tab_admin = tabs[4] if usr == "eric" else None

    # 1. MI PERFIL
    with tab_perfil:
        st.header(f"👤 Perfil de {usr.capitalize()}")
        st.metric("Saldo Actual", f"{usr_data['creditos']} cr")
        
        if usuario_bloqueado:
            st.error(f"🔒 Tu cuenta está **bloqueada temporalmente** hasta el **{fecha_fin_bloqueo}**. No puedes ganar ni gastar créditos.")
        
        st.divider()

        if "tarjeta_activa" in st.session_state and st.session_state.tarjeta_activa is not None:
            idx_sel = st.session_state.tarjeta_activa
            if 0 <= idx_sel < len(usr_data["historial"]):
                item_hist = usr_data["historial"][idx_sel]
                ya_usado = item_hist.get("usado", False)

                with st.container(border=True):
                    st.subheader("📜 Tarjeta de Recompensa / Regla")
                    st.caption(f"👤 Usuario: **{usr.capitalize()}**")

                    if ya_usado:
                        estilo = "background: #e0e0e0; color: #616161; border: 2px dashed #9e9e9e;"
                        texto = "✅ ¡ESTA RECOMPENSA YA HA SIDO USADA / COMPLETADA!"
                    else:
                        estilo = "background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); color: #2c3e50;"
                        texto = "🎉 ¡Vale oficial canjeado y activo!"

                    st.markdown(
                        f"""
                        <div style="{estilo} padding: 20px; border-radius: 12px; text-align: center; margin: 10px 0;">
                            <h2 style="margin:0;">{item_hist['actividad']}</h2>
                            <p style="margin-top: 10px; font-weight: bold; font-size: 1.1em;">{texto}</p>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                    st.caption(f"📅 **Fecha de activación:** {item_hist['fecha']}")

                    c_btn1, c_btn2 = st.columns(2)
                    with c_btn1:
                        if st.button("Marcar como Usado ✅", use_container_width=True, disabled=ya_usado, type="primary"):
                            usr_data["historial"][idx_sel]["usado"] = True
                            guardar_datos(db)
                            st.toast("¡Recompensa completada!", icon="✔")
                            st.rerun()
                    with c_btn2:
                        if st.button("Cerrar tarjeta ❌", use_container_width=True):
                            st.session_state.tarjeta_activa = None
                            st.rerun()
                st.divider()
            else:
                st.session_state.tarjeta_activa = None

        st.subheader("📜 Historial de Actividad")
        if not usr_data["historial"]:
            st.info("Sin movimientos recientes")
        else:
            st.caption("Pulsa sobre cualquier canje para abrir su tarjeta oficial:")
            elementos_historial = list(enumerate(usr_data["historial"]))

            for idx_real, item in reversed(elementos_historial[-10:]):
                c = item.get("coste", 0)
                es_gasto = c > 0
                signo = f"-{c} cr" if es_gasto else (f"+{abs(c)} cr" if c < 0 else "0 cr")
                usado = item.get("usado", False)

                col_h1, col_h2 = st.columns([3, 1])
                with col_h1:
                    if es_gasto:
                        etiqueta = f"✅ {item['actividad']} (Usado)" if usado else f"🎴 {item['actividad']}"
                        if st.button(etiqueta, key=f"btn_card_{idx_real}", use_container_width=True):
                            st.session_state.tarjeta_activa = idx_real
                            st.rerun()
                    else:
                        st.text(f"💪 {item['actividad']}")
                with col_h2:
                    st.caption(f"`{signo}`\n{item['fecha']}")
                st.divider()

        st.subheader("💡 Enviar una Sugerencia")
        if "sug_key" not in st.session_state:
            st.session_state.sug_key = 0

        sugerencia_txt = st.text_area(
            "Escribe tu sugerencia aquí", 
            key=f"input_sugerencia_{st.session_state.sug_key}", 
            placeholder="Ej: Añadir una recompensa para ir al cine..."
        ).strip()
        
        if st.button("Enviar Sugerencia 📩"):
            if sugerencia_txt:
                nueva_sug = {
                    "usuario": usr.capitalize(),
                    "texto": sugerencia_txt,
                    "fecha": obtener_fecha_hora()
                }
                db.setdefault("sugerencias", []).append(nueva_sug)
                guardar_datos(db)
                st.session_state.sug_key += 1
                st.toast("✅ Sugerencia enviada correctamente. ¡Muchas gracias!", icon="🎉")
                st.rerun()
            else:
                st.warning("Por favor, escribe algo antes de enviar.")

    # 2. GANAR CRÉDITOS
    with tab_ganar:
        st.subheader("Completa tareas para ganar créditos")
        if usuario_bloqueado:
            st.error(f"🔒 **Cuenta bloqueada.** No puedes realizar tareas hasta el **{fecha_fin_bloqueo}**.")
        
        search_ganar = st.text_input("🔍 Buscar tarea...", key="search_ganar").strip().lower()
        fecha_hoy = datetime.now(ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d")
        stock = usr_data.setdefault("stock_usado", {}).setdefault(fecha_hoy, {})

        cat_ganar = db.get("catalogo_ganar", CATALOGO_GANAR)
        tareas_filtradas = [t for t in cat_ganar if search_ganar in t["nombre"].lower()]

        if not tareas_filtradas:
            st.info("No se encontraron tareas con esa búsqueda.")
        else:
            for item in tareas_filtradas:
                usados = stock.get(str(item["id"]), 0)
                disp = item["limite_diario"] - usados
                puede_hacer = (disp > 0) and (not usuario_bloqueado)
                
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"**{item['emoji']} {item['nombre']}** \n`+{item['recompensa']} cr` | Disponibles: {disp}/{item['limite_diario']}")
                with c2:
                    if st.button("Completar", key=f"ganar_{item['id']}", disabled=not puede_hacer):
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
        if usuario_bloqueado:
            st.error(f"🔒 **Cuenta bloqueada.** No puedes canjear recompensas hasta el **{fecha_fin_bloqueo}**.")
            
        search_gastar = st.text_input("🔍 Buscar recompensa...", key="search_gastar").strip().lower()
        fecha_hoy = datetime.now(ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d")
        stock = usr_data.setdefault("stock_usado", {}).setdefault(fecha_hoy, {})

        cat_gastar = db.get("catalogo_gastar", CATALOGO_GASTAR)
        recompensas_filtradas = [r for r in cat_gastar if search_gastar in r["nombre"].lower()]

        if not recompensas_filtradas:
            st.info("No se encontraron recompensas con esa búsqueda.")
        else:
            for item in recompensas_filtradas:
                usados = stock.get(str(item["id"]), 0)
                disp = item["limite_diario"] - usados
                puedes_comprar = disp > 0 and usr_data["creditos"] >= item["coste"] and (not usuario_bloqueado)
                es_destacado = item.get("destacado", False)
                
                c1, c2 = st.columns([3, 1])
                with c1:
                    if es_destacado:
                        st.markdown(f"""
                            <div style="background-color: #fff9c4; padding: 10px; border-radius: 8px; border-left: 5px solid #fbc02d; color: #333;">
                                <strong>⭐ {item['emoji']} {item['nombre']}</strong><br>
                                <small><code>Coste: {item['coste']} cr</code> | Disponibles: {disp}/{item['limite_diario']}</small>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"**{item['emoji']} {item['nombre']}** \n`Coste: {item['coste']} cr` | Disponibles: {disp}/{item['limite_diario']}")
                
                with c2:
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

        st.divider()

        solis = usr_data.get("solicitudes_recibidas", [])
        if solis:
            st.subheader("📬 Solicitudes Pendientes")
            for idx, s in enumerate(list(set(solis))):
                c1, c2, c3 = st.columns([2, 1, 1])
                c1.write(f"👤 **{s.capitalize()}**")
                
                if c2.button("Aceptar ✅", key=f"ac_{idx}_{s}"):
                    usr_data["solicitudes_recibidas"] = [x for x in usr_data["solicitudes_recibidas"] if x != s]
                    usr_data["amigos"] = list(dict.fromkeys(usr_data.get("amigos", []) + [s]))
                    db["usuarios"][s]["amigos"] = list(dict.fromkeys(db["usuarios"][s].get("amigos", []) + [usr]))
                    guardar_datos(db)
                    st.toast(f"¡{s.capitalize()} y tú ahora sois amigos!", icon="🤝")
                    st.rerun()
                    
                if c3.button("Rechazar ❌", key=f"rec_{idx}_{s}"):
                    usr_data["solicitudes_recibidas"] = [x for x in usr_data["solicitudes_recibidas"] if x != s]
                    guardar_datos(db)
                    st.rerun()
            st.divider()

        st.subheader("👥 Tu Comunidad")
        amigos = list(dict.fromkeys(usr_data.get("amigos", [])))
        usr_data["amigos"] = amigos
        
        if not amigos:
            st.info("Aún no tienes miembros en tu comunidad.")
        else:
            for idx, a in enumerate(amigos):
                data_a = db["usuarios"].get(a, {})
                with st.expander(f"👤 {a.capitalize()} — Saldo: {data_a.get('creditos', 0)} cr"):
                    max_tr = max(1, usr_data["creditos"])
                    monto = st.number_input(
                        f"Transferir créditos a {a.capitalize()}", 
                        min_value=1, 
                        max_value=max_tr, 
                        key=f"tr_{idx}_{a}"
                    )
                    if st.button(f"Enviar a {a.capitalize()}", key=f"btn_tr_{idx}_{a}", disabled=usuario_bloqueado):
                        if usr_data["creditos"] >= monto:
                            usr_data["creditos"] -= monto
                            data_a["creditos"] += monto
                            f_act = obtener_fecha_hora()
                            usr_data["historial"].append({"actividad": f"💸 Envío a {a.capitalize()}", "coste": monto, "fecha": f_act})
                            data_a.setdefault("historial", []).append({"actividad": f"🎁 Recibido de {usr.capitalize()}", "coste": -monto, "fecha": f_act})
                            guardar_datos(db)
                            st.success(f"¡Enviados {monto} créditos!")
                            st.rerun()
                        else:
                            st.error("No tienes suficientes créditos")

    # 5. PESTAÑA EXCLUSIVA DE ADMIN (solo visible para 'eric')
    if usr == "eric" and tab_admin is not None:
        with tab_admin:
            st.header("⚙️ Consola de Administración")
            st.caption("Acceso exclusivo para moderar créditos, subastas y catálogos.")

            lista_usuarios = list(db["usuarios"].keys())
            u_mod = st.selectbox("Selecciona un usuario a gestionar", lista_usuarios, key="adm_u_mod")
            usr_target = db["usuarios"][u_mod]
            saldo_actual = usr_target.get("creditos", 0)

            # --- SECCIÓN 1: GESTIÓN DE CRÉDITOS ---
            st.subheader("💰 Modificar Créditos")
            st.write(f"Saldo actual de **{u_mod.capitalize()}**: `{saldo_actual} cr`")

            col_adm1, col_adm2 = st.columns(2)
            with col_adm1:
                puntos_mod = st.number_input("Cantidad de créditos", min_value=1, value=10, step=5, key="adm_pts")
                motivo_mod = st.text_input("Motivo del ajuste (opcional)", placeholder="Ej: Penalización por no limpiar", key="adm_motivo")
            
            with col_adm2:
                st.write("Acciones:")
                if st.button("➕ Añadir Puntos", use_container_width=True):
                    usr_target["creditos"] += puntos_mod
                    f_act = obtener_fecha_hora()
                    msg = f"⚡ Ajuste Admin (+{puntos_mod} cr)" + (f": {motivo_mod}" if motivo_mod else "")
                    usr_target.setdefault("historial", []).append({"actividad": msg, "coste": -puntos_mod, "fecha": f_act})
                    guardar_datos(db)
                    st.success(f"¡Añadidos {puntos_mod} cr a {u_mod.capitalize()}!")
                    st.rerun()

                if st.button("➖ Quitar Puntos", type="primary", use_container_width=True):
                    usr_target["creditos"] = max(0, usr_target["creditos"] - puntos_mod)
                    f_act = obtener_fecha_hora()
                    msg = f"⚠️ Penalización Admin (-{puntos_mod} cr)" + (f": {motivo_mod}" if motivo_mod else "")
                    usr_target.setdefault("historial", []).append({"actividad": msg, "coste": puntos_mod, "fecha": f_act})
                    guardar_datos(db)
                    st.warning(f"¡Restados {puntos_mod} cr a {u_mod.capitalize()}!")
                    st.rerun()

            st.divider()

            # --- SECCIÓN 2: SUBASTAS Y PUJAS ---
            st.subheader("🔨 Gestión de Subastas Semanales")
            subasta_act = db.get("subasta_activa")

            if subasta_act and subasta_act.get("activa"):
                st.warning(f"🔨 **Subasta en curso:** {subasta_act['item']}")
                st.write(f"• Puja actual: `{subasta_act['puja_actual']} cr`")
                st.write(f"• Liderando: **{subasta_act['max_postor'].capitalize() if subasta_act['max_postor'] else 'Nadie'}**")

                c_sub_a1, c_sub_a2 = st.columns(2)
                with c_sub_a1:
                    if st.button("🏁 Finalizar y Adjudicar Premio", type="primary", use_container_width=True):
                        ganador = subasta_act.get("max_postor")
                        precio_final = subasta_act.get("puja_actual", 0)
                        item_nombre = subasta_act.get("item")

                        if ganador and ganador in db["usuarios"]:
                            usr_ganador = db["usuarios"][ganador]
                            if usr_ganador["creditos"] >= precio_final:
                                usr_ganador["creditos"] -= precio_final
                                f_act = obtener_fecha_hora()
                                usr_ganador.setdefault("historial", []).append({
                                    "actividad": f"🏆 Ganador Subasta: {item_nombre}",
                                    "coste": precio_final,
                                    "fecha": f_act
                                })
                                db["subasta_activa"] = None
                                guardar_datos(db)
                                st.success(f"¡Subasta finalizada! {ganador.capitalize()} gana {item_nombre} por {precio_final} cr.")
                                st.rerun()
                            else:
                                st.error(f"{ganador.capitalize()} ya no tiene créditos suficientes para pagar ({precio_final} cr).")
                        else:
                            db["subasta_activa"] = None
                            guardar_datos(db)
                            st.info("Subasta cancelada sin ganador.")
                            st.rerun()

                with c_sub_a2:
                    if st.button("❌ Cancelar Subasta (Sin Ganador)", use_container_width=True):
                        db["subasta_activa"] = None
                        guardar_datos(db)
                        st.info("Subasta cancelada.")
                        st.rerun()
            else:
                st.caption("Crea una subasta especial para que los usuarios compitan por un premio.")
                item_subasta = st.text_input("Recompensa a subastar", placeholder="Ej: Elegir el menú del fin de semana", key="adm_sub_item")
                puja_salida = st.number_input("Precio de salida (cr)", min_value=5, value=20, step=5, key="adm_sub_salida")

                if st.button("🚀 Lanzar Nueva Subasta", type="primary"):
                    if item_subasta.strip():
                        db["subasta_activa"] = {
                            "item": item_subasta.strip(),
                            "puja_actual": int(puja_salida),
                            "max_postor": None,
                            "activa": True
                        }
                        guardar_datos(db)
                        st.success("¡Subasta publicada!")
                        st.rerun()
                    else:
                        st.error("Introduce la descripción del premio a subastar.")

            st.divider()

            # --- SECCIÓN 3: BLOQUEO TEMPORAL DE CUENTA ---
            st.subheader("🔒 Bloquear / Desbloquear Cuenta")
            esta_bl, f_fin_bl = esta_bloqueado(usr_target)
            
            if esta_bl:
                st.warning(f"⚠️ **{u_mod.capitalize()}** está actualmente **BLOQUEADO** hasta el {f_fin_bl}.")
                if st.button(f"🔓 Desbloquear a {u_mod.capitalize()} ahora mismo", type="primary"):
                    usr_target["bloqueado_hasta"] = None
                    guardar_datos(db)
                    st.success(f"¡{u_mod.capitalize()} ha sido desbloqueado!")
                    st.rerun()
            else:
                st.info(f"🟢 **{u_mod.capitalize()}** tiene la cuenta activa y sin restricciones.")
                
                col_b1, col_b2 = st.columns(2)
                with col_b1:
                    fecha_bloqueo = st.date_input("Bloquear hasta el día", key="adm_f_blq")
                with col_b2:
                    hora_bloqueo = st.time_input("Hora de fin", key="adm_h_blq")
                
                if st.button(f"🔒 Aplicar Bloqueo a {u_mod.capitalize()}", use_container_width=True):
                    dt_bloqueo = datetime.combine(fecha_bloqueo, hora_bloqueo, tzinfo=ZoneInfo("Europe/Madrid"))
                    ahora = datetime.now(ZoneInfo("Europe/Madrid"))
                    if dt_bloqueo <= ahora:
                        st.error("La fecha/hora de bloqueo debe ser futura.")
                    else:
                        usr_target["bloqueado_hasta"] = dt_bloqueo.isoformat()
                        guardar_datos(db)
                        st.success(f"¡Cuenta de {u_mod.capitalize()} bloqueada hasta el {dt_bloqueo.strftime('%d/%m/%Y a las %H:%M')}!")
                        st.rerun()

            st.divider()

            # --- SECCIÓN 4: RETOS DIARIOS / DESAFÍOS ---
            st.subheader("🎯 Retos Diarios / Desafíos de Administrador")
            st.caption("Publica una misión flash que verán todos los usuarios en la pantalla principal.")
            
            reto_actual = db.get("reto_flash")
            if reto_actual and reto_actual.get("activo"):
                st.warning(f"🔥 **Reto activo:** {reto_actual['texto']} (+{reto_actual['recompensa']} cr)")
                if st.button("❌ Cancelar / Desactivar Reto", key="btn_cancelar_reto"):
                    db["reto_flash"] = None
                    guardar_datos(db)
                    st.success("Reto desactivado.")
                    st.rerun()
            else:
                texto_reto = st.text_input("Descripción del reto flash", placeholder="Ej: El primero en sacar la basura gana puntos doble", key="adm_ret_txt")
                puntos_reto = st.number_input("Recompensa extra", min_value=1, value=25, key="adm_ret_pts")
                if st.button("📢 Publicar Reto Global", type="primary"):
                    if texto_reto.strip():
                        db["reto_flash"] = {
                            "texto": texto_reto.strip(),
                            "recompensa": int(puntos_reto),
                            "activo": True
                        }
                        guardar_datos(db)
                        st.success("¡Reto publicado para todos los usuarios!")
                        st.rerun()
                    else:
                        st.error("Introduce una descripción para el reto.")

            st.divider()

            # --- SECCIÓN 5: GESTOR Y EDITOR DE CATÁLOGOS ---
            st.subheader("🎨 Gestor y Editor de Catálogos")
            tab_cat1, tab_cat2 = st.tabs(["➕ Añadir Elemento", "✏️ Modificar / Eliminar Existente"])

            with tab_cat1:
                tipo_cat = st.radio("¿Dónde deseas añadirlo?", ["🛒 Gastar (Recompensa)", "💪 Ganar (Tarea)"], horizontal=True, key="adm_rad_add")

                c_n1, c_n2 = st.columns([1, 3])
                with c_n1:
                    nuevo_emoji = st.text_input("Emoji", value="✨", key="adm_emoji")
                with c_n2:
                    nuevo_nombre = st.text_input("Nombre de la tarea/premio", key="adm_nombre")

                c_n3, c_n4 = st.columns(2)
                with c_n3:
                    nuevo_valor = st.number_input("Valor en Créditos", min_value=1, value=15, key="adm_valor")
                with c_n4:
                    nuevo_limite = st.number_input("Límite diario", min_value=1, value=1, key="adm_limite")

                es_destacado = st.checkbox("⭐ Destacar elemento", key="adm_destacado")

                if st.button("Guardar en el Catálogo 💾", type="primary", key="btn_guardar_nuevo_cat"):
                    if not nuevo_nombre:
                        st.error("Por favor, introduce un nombre.")
                    else:
                        if tipo_cat.startswith("🛒"):
                            lista_cat = db.get("catalogo_gastar", CATALOGO_GASTAR)
                            nuevo_id = max([x["id"] for x in lista_cat], default=0) + 1
                            nuevo_item = {
                                "id": nuevo_id,
                                "emoji": nuevo_emoji,
                                "nombre": nuevo_nombre,
                                "coste": int(nuevo_valor),
                                "limite_diario": int(nuevo_limite)
                            }
                            if es_destacado:
                                nuevo_item["destacado"] = True
                            lista_cat.append(nuevo_item)
                            db["catalogo_gastar"] = lista_cat
                        else:
                            lista_cat = db.get("catalogo_ganar", CATALOGO_GANAR)
                            nuevo_id = max([x["id"] for x in lista_cat], default=100) + 1
                            nuevo_item = {
                                "id": nuevo_id,
                                "emoji": nuevo_emoji,
                                "nombre": nuevo_nombre,
                                "recompensa": int(nuevo_valor),
                                "limite_diario": int(nuevo_limite)
                            }
                            if es_destacado:
                                nuevo_item["destacado"] = True
                            lista_cat.append(nuevo_item)
                            db["catalogo_ganar"] = lista_cat

                        guardar_datos(db)
                        st.toast("¡Elemento añadido al catálogo con éxito!", icon="🎉")
                        st.rerun()

            with tab_cat2:
                tipo_cat_edit = st.radio("Selecciona catálogo a modificar", ["🛒 Recompensas (Gastar)", "💪 Tareas (Ganar)"], horizontal=True, key="adm_rad_edit")
                
                es_tienda = tipo_cat_edit.startswith("🛒")
                lista_editar = db.get("catalogo_gastar" if es_tienda else "catalogo_ganar", CATALOGO_GASTAR if es_tienda else CATALOGO_GANAR)
                
                nombres_items = [f"{x['emoji']} {x['nombre']} (ID: {x['id']})" for x in lista_editar]
                item_seleccionado_str = st.selectbox("Elige un elemento para editar o borrar", nombres_items, key="adm_sel_item_edit")

                if item_seleccionado_str:
                    id_sel = int(item_seleccionado_str.split("ID: ")[1].replace(")", ""))
                    item_obj = next((x for x in lista_editar if x["id"] == id_sel), None)

                    if item_obj:
                        with st.form(key=f"form_edit_{id_sel}"):
                            st.write(f"✏️ **Editando:** {item_obj['nombre']}")
                            e_emoji = st.text_input("Emoji", value=item_obj.get("emoji", "✨"))
                            e_nombre = st.text_input("Nombre", value=item_obj.get("nombre", ""))
                            val_clave = "coste" if es_tienda else "recompensa"
                            e_valor = st.number_input("Créditos", min_value=1, value=int(item_obj.get(val_clave, 10)))
                            e_limite = st.number_input("Límite diario", min_value=1, value=int(item_obj.get("limite_diario", 1)))
                            e_destacado = st.checkbox("⭐ Destacado", value=item_obj.get("destacado", False))

                            c_save, c_del = st.columns(2)
                            with c_save:
                                submit_save = st.form_submit_button("💾 Guardar Cambios", type="primary", use_container_width=True)
                            with c_del:
                                submit_del = st.form_submit_button("🗑️ Eliminar Elemento", use_container_width=True)

                            if submit_save:
                                item_obj["emoji"] = e_emoji
                                item_obj["nombre"] = e_nombre
                                item_obj[val_clave] = int(e_valor)
                                item_obj["limite_diario"] = int(e_limite)
                                item_obj["destacado"] = e_destacado
                                guardar_datos(db)
                                st.toast("¡Elemento actualizado!", icon="✅")
                                st.rerun()

                            if submit_del:
                                if es_tienda:
                                    db["catalogo_gastar"] = [x for x in db["catalogo_gastar"] if x["id"] != id_sel]
                                else:
                                    db["catalogo_ganar"] = [x for x in db["catalogo_ganar"] if x["id"] != id_sel]
                                guardar_datos(db)
                                st.toast("¡Elemento eliminado!", icon="🗑️")
                                st.rerun()

            st.divider()

            # --- SECCIÓN 6: AUDITORÍA DE ACTIVIDAD INTEGRAL ---
            st.subheader("📜 Auditoría Global de Actividad")
            st.caption("Muestra todos los movimientos registrados en la app por orden cronológico.")

            actividades_totales = []
            for nombre_usr, datos_usr in db["usuarios"].items():
                for item_h in datos_usr.get("historial", []):
                    actividades_totales.append({
                        "usuario": nombre_usr.capitalize(),
                        "actividad": item_h.get("actividad", ""),
                        "coste": item_h.get("coste", 0),
                        "fecha": item_h.get("fecha", "")
                    })

            if not actividades_totales:
                st.info("Aún no hay registros de actividad globales.")
            else:
                for act in reversed(actividades_totales[-20:]):
                    c = act["coste"]
                    signo = f"-{c} cr" if c > 0 else (f"+{abs(c)} cr" if c < 0 else "0 cr")
                    
                    c_aud1, c_aud2 = st.columns([3, 1])
                    with c_aud1:
                        st.markdown(f"👤 **{act['usuario']}** — {act['actividad']}")
                    with c_aud2:
                        st.caption(f"`{signo}` | {act['fecha']}")
                    st.divider()

            # --- SECCIÓN 7: SUGERENCIAS RECIBIDAS ---
            st.subheader("📥 Sugerencias Recibidas")
            if st.button("Vaciar todas las sugerencias 🗑️", key="btn_vaciar_sug_adm"):
                db["sugerencias"] = []
                guardar_datos(db)
                st.rerun()

            sugerencias_lista = db.get("sugerencias", [])
            if not sugerencias_lista:
                st.info("No hay sugerencias registradas por ahora.")
            else:
                for sug in reversed(sugerencias_lista):
                    st.markdown(f"**👤 {sug['usuario']}** ({sug['fecha']}):\n> {sug['texto']}")
                    st.divider()

# Ejecución
renderizar_panel_principal()
