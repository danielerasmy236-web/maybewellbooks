/* Legal page content for Maybewell Books.
 * Loaded as a plain global before the app bundle so the (minified, no-build)
 * React app can read window.__MW_LEGAL__[lang][page] without embedding this
 * much text inside the hard-to-edit bundle file itself.
 *
 * Drafted to accurately reflect what this site actually does technically:
 * Lemon Squeezy as Merchant of Record for payment/tax, Resend for delivery
 * email, cart/wishlist/library kept in browser localStorage (not a server
 * account), no ad trackers. Not legal advice — have a lawyer in your
 * operating jurisdiction review before you rely on this for real sales,
 * especially the refund and governing-law sections.
 */
window.__MW_LEGAL__ = {
  en: {
    updated: "Last updated: July 2026",
    privacy: [
      { h: "Overview", b: "Maybewell Books (“we,” “us”) sells printable PDF activity books at maybewellbooks.com. This policy explains what information we collect when you browse or buy from us, why we collect it, and the choices you have." },
      { h: "Information We Collect", b: "Account-free by design: we don't require you to create an account. When you buy something, we collect the email address you provide at checkout (so we can send your files), and Lemon Squeezy — our payment processor — collects your payment details directly; we never see or store your card number. If you join our monthly letter, we collect the email you submit. Our hosting provider (Netlify) automatically logs basic technical data for every visitor, like IP address and browser type, for security and performance — the same as almost any website. Your cart, wishlist, and “My library” list live only in your browser's local storage; they are never transmitted to our servers." },
      { h: "How We Use Your Information", b: "We use your email to deliver the PDFs you purchase, send order confirmations, and respond if you contact us. If you opt into the monthly letter, we use your email to send it — and nothing else. We do not use your information for advertising, and we do not build profiles for targeting." },
      { h: "How Purchases Are Processed", b: "Checkout happens on Lemon Squeezy's platform, which acts as the Merchant of Record for every sale: they handle payment processing, fraud checks, and sales tax/VAT/GST collection in your country. Lemon Squeezy has its own privacy policy governing the payment information you give them directly." },
      { h: "Email Delivery", b: "We use Resend to send order and newsletter emails. Resend processes your email address solely to deliver our messages and does not use it for any other purpose." },
      { h: "Cookies & Local Storage", b: "See our separate Cookie Policy for the full detail — in short, we use your browser's local storage (not tracking cookies) to remember your cart and wishlist between visits." },
      { h: "Data Sharing", b: "We never sell your information. We share it only with the service providers named above (Lemon Squeezy, Resend, Netlify), each solely to perform the task we hired them for." },
      { h: "Data Retention", b: "We keep order and email records as long as needed for accounting, tax, and customer support purposes, and delete or anonymize them when no longer needed. You can ask us to delete your data sooner — see “Your Rights” below." },
      { h: "Your Rights", b: "You can ask us to access, correct, or delete the personal information we hold about you, and you can unsubscribe from the monthly letter at any time via the link in every email. To make any request, email hello@maybewellbooks.com — we'll respond within 30 days." },
      { h: "Children's Privacy", b: "Many of our books are designed for kids to use with a grown-up's help, but purchases are made by adults, and we don't knowingly collect personal information directly from children. If you believe a child has given us personal information, contact us and we'll delete it." },
      { h: "International Users", b: "We're based in the United States and primarily serve customers there and across Southeast Asia. Your information may be processed in the United States and in the countries where our service providers operate." },
      { h: "Changes to This Policy", b: "If we make material changes, we'll update the date at the top of this page. Continued use of the site after a change means you accept the update." },
      { h: "Contact Us", b: "Questions about this policy? Email hello@maybewellbooks.com." },
    ],
    terms: [
      { h: "Agreement to These Terms", b: "By buying from or using maybewellbooks.com, you agree to these Terms of Service. If you don't agree, please don't use the site." },
      { h: "What We Sell", b: "We sell printable PDF activity books — digital files delivered by email after purchase. Nothing physical is shipped." },
      { h: "Purchases & Payment", b: "All purchases are processed by Lemon Squeezy, our Merchant of Record, who handles payment, invoicing, and applicable sales tax. Prices are shown in USD; Lemon Squeezy may display your local currency equivalent at checkout." },
      { h: "Delivery", b: "After payment confirms, we email your download link(s) to the address you provide at checkout, usually within a few minutes. If nothing arrives within 24 hours, check your spam folder, then contact us at hello@maybewellbooks.com and we'll sort it out." },
      { h: "Your License to Use What You Buy", b: "When you buy a book, we grant you a license to print and use it for personal, family, or single-classroom use — print as many physical copies as you like for that use. You may not resell, redistribute, or share the PDF file itself (as an email attachment, upload, file share, etc.), repost it publicly, or use it to create a competing product. Every book remains the intellectual property of Maybewell Books." },
      { h: "Refunds", b: "Because our books are instant digital downloads, all sales are final once a file is delivered. If your download link doesn't work, the file is corrupted, or you were charged but never received your email, contact us within 14 days of purchase and we'll fix it or refund you — whichever makes sense." },
      { h: "Acceptable Use", b: "Don't use the site to do anything illegal, attempt to disrupt or reverse-engineer it, or infringe on anyone else's rights." },
      { h: "Availability & Changes", b: "We may add, remove, or change products, prices, or features at any time. We'll never change what's included in a book you've already purchased in a way that reduces its value to you." },
      { h: "Disclaimer & Limitation of Liability", b: "The site and its products are provided “as is.” To the extent permitted by law, Maybewell Books isn't liable for indirect or consequential damages arising from your use of the site or its products. Our total liability for any claim is limited to the amount you paid us for the product in question." },
      { h: "Governing Law", b: "These terms are governed by the laws of the United States, without regard to conflict-of-law principles, except where local consumer protection law gives you rights we can't override." },
      { h: "Changes to These Terms", b: "We may update these terms occasionally; the “Last updated” date at the top will reflect the latest version. Continuing to use the site after a change means you accept it." },
      { h: "Contact Us", b: "Questions about these terms? Email hello@maybewellbooks.com." },
    ],
    cookies: [
      { h: "The Short Version", b: "This site mostly avoids tracking cookies altogether. What keeps your cart and wishlist working between visits is your browser's local storage, not a cookie — the difference matters, so we've explained it below rather than pasting a generic cookie notice." },
      { h: "What We Actually Use", b: "Local storage (not a cookie): your cart, wishlist, and “My library” are saved directly in your browser and never leave your device unless you complete a purchase. Clearing your browser's site data removes them instantly. Essential hosting: our host, Netlify, may set a small functional cookie or use similar technology strictly to serve the site correctly and securely — this isn't used to track you across other sites." },
      { h: "What Happens When You Check Out", b: "When you click “Buy now,” you're taken to a checkout page hosted by Lemon Squeezy, which is a separate site with its own cookies for processing your payment securely. Their use of cookies is covered by Lemon Squeezy's own policy, not ours." },
      { h: "What We Don't Use", b: "No advertising cookies, no third-party analytics trackers, and no cross-site tracking of any kind at this time. If that ever changes, we'll update this page and this section first." },
      { h: "Managing Your Data", b: "You can clear your cart, wishlist, and library at any time by clearing your browser's local storage for maybewellbooks.com (usually in your browser's site settings, or by using private/incognito browsing)." },
      { h: "Changes to This Policy", b: "If we start using additional cookies or trackers in the future, we'll update this page and the date below." },
      { h: "Contact Us", b: "Questions? Email hello@maybewellbooks.com." },
    ],
  },
  es: {
    updated: "Última actualización: julio de 2026",
    privacy: [
      { h: "Resumen", b: "Maybewell Books (“nosotros”) vende libros de actividades en PDF imprimibles en maybewellbooks.com. Esta política explica qué información recopilamos cuando navegas o compras, por qué la recopilamos, y qué opciones tienes." },
      { h: "Información que Recopilamos", b: "Sin cuentas por diseño: no necesitas crear una cuenta. Cuando compras algo, recopilamos el correo que nos das al pagar (para enviarte tus archivos), y Lemon Squeezy — nuestro procesador de pagos — recopila tus datos de pago directamente; nosotros nunca vemos ni guardamos el número de tu tarjeta. Si te unes a nuestra carta mensual, recopilamos el correo que ingreses. Nuestro proveedor de hosting (Netlify) registra automáticamente datos técnicos básicos de cada visitante, como la dirección IP y el tipo de navegador, por seguridad y rendimiento — igual que casi cualquier sitio web. Tu carrito, lista de deseos, y “Mi biblioteca” viven solo en el almacenamiento local de tu navegador; nunca se envían a nuestros servidores." },
      { h: "Cómo Usamos tu Información", b: "Usamos tu correo para entregarte los PDFs que compras, enviarte confirmaciones de pedido, y responderte si nos contactas. Si te suscribes a la carta mensual, usamos tu correo para enviarla — y nada más. No usamos tu información para publicidad, ni construimos perfiles para segmentación." },
      { h: "Cómo se Procesan las Compras", b: "El pago ocurre en la plataforma de Lemon Squeezy, que actúa como Merchant of Record de cada venta: ellos manejan el procesamiento del pago, verificaciones de fraude, y la recaudación de impuestos de venta/IVA en tu país. Lemon Squeezy tiene su propia política de privacidad que rige la información de pago que les das directamente." },
      { h: "Entrega por Correo", b: "Usamos Resend para enviar correos de pedidos y de la carta mensual. Resend procesa tu correo únicamente para entregar nuestros mensajes y no lo usa para ningún otro fin." },
      { h: "Cookies y Almacenamiento Local", b: "Consulta nuestra Política de Cookies separada para el detalle completo — en resumen, usamos el almacenamiento local de tu navegador (no cookies de rastreo) para recordar tu carrito y lista de deseos entre visitas." },
      { h: "Compartir Datos", b: "Nunca vendemos tu información. Solo la compartimos con los proveedores de servicio mencionados arriba (Lemon Squeezy, Resend, Netlify), cada uno únicamente para la tarea que le contratamos." },
      { h: "Retención de Datos", b: "Conservamos los registros de pedidos y correos el tiempo necesario para fines contables, fiscales, y de soporte al cliente, y los eliminamos o anonimizamos cuando ya no se necesitan. Puedes pedirnos que eliminemos tus datos antes — ve “Tus Derechos” abajo." },
      { h: "Tus Derechos", b: "Puedes pedirnos acceder, corregir, o eliminar la información personal que tenemos sobre ti, y puedes darte de baja de la carta mensual en cualquier momento con el enlace en cada correo. Para cualquier solicitud, escribe a hello@maybewellbooks.com — responderemos dentro de 30 días." },
      { h: "Privacidad de Menores", b: "Muchos de nuestros libros están diseñados para que los niños los usen con ayuda de un adulto, pero las compras las hacen adultos, y no recopilamos a sabiendas información personal directamente de menores. Si crees que un menor nos dio información personal, contáctanos y la eliminaremos." },
      { h: "Usuarios Internacionales", b: "Estamos en Estados Unidos y atendemos principalmente a clientes ahí y en el sudeste asiático. Tu información puede procesarse en Estados Unidos y en los países donde operan nuestros proveedores de servicio." },
      { h: "Cambios a esta Política", b: "Si hacemos cambios importantes, actualizaremos la fecha al inicio de esta página. Seguir usando el sitio después de un cambio significa que aceptas la actualización." },
      { h: "Contáctanos", b: "¿Preguntas sobre esta política? Escribe a hello@maybewellbooks.com." },
    ],
    terms: [
      { h: "Aceptación de estos Términos", b: "Al comprar o usar maybewellbooks.com, aceptas estos Términos de Servicio. Si no estás de acuerdo, por favor no uses el sitio." },
      { h: "Qué Vendemos", b: "Vendemos libros de actividades en PDF imprimibles — archivos digitales entregados por correo después de la compra. No se envía nada físico." },
      { h: "Compras y Pago", b: "Todas las compras las procesa Lemon Squeezy, nuestro Merchant of Record, quien maneja el pago, la facturación, y los impuestos de venta aplicables. Los precios se muestran en USD; Lemon Squeezy puede mostrar el equivalente en tu moneda local al pagar." },
      { h: "Entrega", b: "Después de confirmar el pago, te enviamos por correo tu(s) enlace(s) de descarga a la dirección que diste al pagar, usualmente en unos minutos. Si no llega nada en 24 horas, revisa tu carpeta de spam, y luego contáctanos a hello@maybewellbooks.com y lo resolvemos." },
      { h: "Tu Licencia de Uso", b: "Cuando compras un libro, te otorgamos una licencia para imprimirlo y usarlo de forma personal, familiar, o en un solo salón de clase — imprime tantas copias físicas como quieras para ese uso. No puedes revender, redistribuir, o compartir el archivo PDF en sí (como adjunto de correo, subida, archivo compartido, etc.), republicarlo públicamente, ni usarlo para crear un producto competidor. Cada libro sigue siendo propiedad intelectual de Maybewell Books." },
      { h: "Reembolsos", b: "Como nuestros libros son descargas digitales instantáneas, todas las ventas son finales una vez entregado el archivo. Si tu enlace de descarga no funciona, el archivo está dañado, o te cobraron pero nunca recibiste tu correo, contáctanos dentro de 14 días de la compra y lo arreglamos o te reembolsamos — lo que tenga más sentido." },
      { h: "Uso Aceptable", b: "No uses el sitio para hacer nada ilegal, intentar interrumpirlo o hacerle ingeniería inversa, ni infringir los derechos de alguien más." },
      { h: "Disponibilidad y Cambios", b: "Podemos agregar, quitar, o cambiar productos, precios, o funciones en cualquier momento. Nunca cambiaremos lo incluido en un libro que ya compraste de una forma que reduzca su valor para ti." },
      { h: "Descargo y Limitación de Responsabilidad", b: "El sitio y sus productos se ofrecen “tal cual.” En la medida permitida por la ley, Maybewell Books no es responsable por daños indirectos o consecuentes derivados de tu uso del sitio o sus productos. Nuestra responsabilidad total por cualquier reclamo se limita al monto que nos pagaste por el producto en cuestión." },
      { h: "Ley Aplicable", b: "Estos términos se rigen por las leyes de Estados Unidos, sin considerar principios de conflicto de leyes, excepto donde la ley local de protección al consumidor te otorgue derechos que no podamos anular." },
      { h: "Cambios a estos Términos", b: "Podemos actualizar estos términos ocasionalmente; la fecha de “Última actualización” arriba reflejará la versión más reciente. Seguir usando el sitio después de un cambio significa que lo aceptas." },
      { h: "Contáctanos", b: "¿Preguntas sobre estos términos? Escribe a hello@maybewellbooks.com." },
    ],
    cookies: [
      { h: "La Versión Corta", b: "Este sitio en su mayoría evita por completo las cookies de rastreo. Lo que mantiene tu carrito y lista de deseos funcionando entre visitas es el almacenamiento local de tu navegador, no una cookie — la diferencia importa, así que la explicamos abajo en vez de pegar un aviso de cookies genérico." },
      { h: "Qué Usamos Realmente", b: "Almacenamiento local (no una cookie): tu carrito, lista de deseos, y “Mi biblioteca” se guardan directamente en tu navegador y nunca salen de tu dispositivo a menos que completes una compra. Borrar los datos del sitio en tu navegador los elimina al instante. Hosting esencial: nuestro host, Netlify, puede usar una pequeña cookie funcional o tecnología similar estrictamente para servir el sitio de forma correcta y segura — esto no se usa para rastrearte en otros sitios." },
      { h: "Qué Pasa al Pagar", b: "Cuando haces clic en “Comprar ahora,” te llevamos a una página de pago alojada por Lemon Squeezy, que es un sitio separado con sus propias cookies para procesar tu pago de forma segura. Su uso de cookies se rige por la propia política de Lemon Squeezy, no la nuestra." },
      { h: "Qué No Usamos", b: "Ninguna cookie publicitaria, ningún rastreador de análisis de terceros, y ningún rastreo entre sitios por ahora. Si eso cambia alguna vez, actualizaremos esta página y esta sección primero." },
      { h: "Administrar tus Datos", b: "Puedes borrar tu carrito, lista de deseos, y biblioteca en cualquier momento borrando el almacenamiento local de tu navegador para maybewellbooks.com (usualmente en la configuración del sitio de tu navegador, o usando modo privado/incógnito)." },
      { h: "Cambios a esta Política", b: "Si empezamos a usar cookies o rastreadores adicionales en el futuro, actualizaremos esta página y la fecha abajo." },
      { h: "Contáctanos", b: "¿Preguntas? Escribe a hello@maybewellbooks.com." },
    ],
  },
};
