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
    {"id": 2, "emoji": "📺", "nombre": "Ver la tele (1h)", "coste": 15, "limite_diario": 3},
    {"id": 3, "emoji": "🃏", "nombre": "Cambiar de juego/regla", "coste": 30, "limite_diario": 2},
    {"id": 4, "emoji": "🍫", "nombre": "Comer dulce", "coste": 15, "limite_diario": 1},
    {"id": 5, "emoji": "🎯", "nombre": "Elegir el primer turno", "coste": 10, "limite_diario": 1},
    {"id": 6, "emoji": "🎵", "nombre": "Elegir musica (1h)", "coste": 10, "limite_diario": 2},
    {"id": 7, "emoji": "🧊", "nombre": "Camarero por un momento", "coste": 20, "limite_diario": 1},
    {"id": 8, "emoji": "🍕", "nombre": "El ingrediente prohibido", "coste": 20, "limite_diario": 1},
    {"id": 9, "emoji": "💆", "nombre": "Masaje 5-10 min", "coste": 10, "limite_diario": 1},
    {"id": 10, "emoji": "🛡️", "nombre": "Inmunidad en un juego", "coste": 20, "limite_diario": 1},
    {"id": 11, "emoji": "🎲", "nombre": "Elegir el juego de mesa de hoy", "coste": 20, "limite_diario": 1},
    {"id": 12, "emoji": "🪞", "nombre": "Carta espejo: Rebotar un favor", "coste": 25, "limite_diario": 1},
    {"id": 13, "emoji": "🤏", "nombre": "Impuesto del 10% de snack", "coste": 10, "limite_diario": 2},
    {"id": 14, "emoji": "🏆", "nombre": "Pase VIP: Fin de semana libre", "coste": 210, "limite_diario": 1, "destacado": True},
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
    """Devuelve la fecha y hora formateada según la zona horaria de Madrid"""
    return datetime.now(ZoneInfo("Europe/Madrid")).strftime("%d/%m/%Y %H:%M")

def cargar_datos():
    try:
        response = supabase.table("estado_app").select("datos").eq("id", 1).execute()
        if response.data and len(response.data) > 0 and response.data[0].get("datos"):
            datos = response.data[0]["datos"]
            
            # Asegurar claves por defecto
            datos.setdefault("sugerencias", [])
            datos.setdefault("usuarios", {})
            
            # Inicializar usuario predeterminado si la BD está completamente vacía
            if not datos["usuarios"]:
                datos = DATOS_INICIALES
                guardar_datos(datos)

            # Comprobación de reinicio semanal
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
                    "solicitudes_recibidas": []
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

    tab_perfil, tab_ganar, tab_tienda, tab_comunidad = st.tabs(["Mi Perfil", "💪 Ganar", "🛒 Gastar", "👥 Comunidad"])

    # 1. PERFIL
    with tab_perfil:
                # --- TARJETA EMERGENTE (MODAL) ---
                # --- CONTROL DE ESTADO DE LA TARJETA ---
        if "tarjeta_activa" not in st.session_state:
            st.session_state.tarjeta_activa = None

        @st.dialog("📜 Tarjeta de Recompensa / Regla")
        def mostrar_tarjeta():
            data = st.session_state.tarjeta_activa
            if not data:
                return
            
            st.markdown(f"### 👤 Usuario: **{data['usuario'].capitalize()}**")
            st.divider()
            
            # Diseño estilo tarjeta de juego
            st.markdown(
                f"""
                <div style="
                    background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
                    padding: 25px;
                    border-radius: 15px;
                    text-align: center;
                    color: #2c3e50;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
                    margin: 10px 0;
                ">
                    <h2 style="margin:0; color: #2c3e50;">{data['actividad']}</h2>
                    <p style="margin-top: 15px; font-weight: bold; font-size: 1.1em;">
                        ¡Vale oficial canjeado y activo!
                    </p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            st.caption(f"📅 **Fecha de activación:** {data['fecha']}")
            st.info("👉 Enseña esta pantalla para hacer valer tu recompensa o regla.")
            
            if st.button("Cerrar tarjeta ❌", use_container_width=True):
                st.session_state.tarjeta_activa = None
                st.rerun()

        # Si hay una tarjeta activa guardada, la mantenemos abierta incluso con el autorefresco
        if st.session_state.tarjeta_activa:
            mostrar_tarjeta()

        # --- HISTORIAL CON BOTONES ---
        st.subheader("📜 Historial de Actividad")
        if not usr_data["historial"]:
            st.info("Sin movimientos recientes")
        else:
            st.caption("Pulsa sobre cualquier canje para abrir su tarjeta oficial:")
            for idx, item in enumerate(reversed(usr_data["historial"][-10:])):
                c = item["coste"]
                es_gasto = c > 0
                signo = f"-{c} cr" if es_gasto else (f"+{abs(c)} cr" if c < 0 else "0 cr")
                
                col_h1, col_h2 = st.columns([3, 1])
                with col_h1:
                    if es_gasto:
                        if st.button(f"🎴 {item['actividad']}", key=f"btn_hist_{idx}", use_container_width=True):
                            # Guardamos los datos de la tarjeta en la sesión
                            st.session_state.tarjeta_activa = {
                                "actividad": item['actividad'],
                                "fecha": item['fecha'],
                                "usuario": usr
                            }
                            st.rerun()
                    else:
                        st.text(f"💪 {item['actividad']}")
                with col_h2:
                    st.caption(f"`{signo}`\n{item['fecha']}")
                st.divider()



        # SUGERENCIAS
        st.subheader("💡 Enviar una Sugerencia")
        st.caption("¿Tienes alguna idea para mejorar la app o sugerir tareas/premios?")
        
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
        
        search_ganar = st.text_input("🔍 Buscar tarea...", key="search_ganar").strip().lower()
        fecha_hoy = datetime.now(ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d")
        stock = usr_data.setdefault("stock_usado", {}).setdefault(fecha_hoy, {})

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
        
        search_gastar = st.text_input("🔍 Buscar recompensa...", key="search_gastar").strip().lower()
        fecha_hoy = datetime.now(ZoneInfo("Europe/Madrid")).strftime("%Y-%m-%d")
        stock = usr_data.setdefault("stock_usado", {}).setdefault(fecha_hoy, {})

        recompensas_filtradas = [r for r in CATALOGO_GASTAR if search_gastar in r["nombre"].lower()]

        if not recompensas_filtradas:
            st.info("No se encontraron recompensas con esa búsqueda.")
        else:
            for item in recompensas_filtradas:
                usados = stock.get(str(item["id"]), 0)
                disp = item["limite_diario"] - usados
                puedes_comprar = disp > 0 and usr_data["creditos"] >= item["coste"]
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
                            data_a.setdefault("historial", []).append({"actividad": f"🎁 Recibido de {usr.capitalize()}", "coste": -monto, "fecha": f_act})
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
