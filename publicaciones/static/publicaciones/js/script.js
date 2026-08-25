document.addEventListener("DOMContentLoaded", () => {

    console.log("ASOPROMUVI cargado correctamente");


    /* =========================================
       ANIMACIONES AL HACER SCROLL
    ========================================= */

    const elementos =
        document.querySelectorAll(".reveal");


    if ("IntersectionObserver" in window) {

        const observer =
            new IntersectionObserver(

                (entries, obs) => {

                    entries.forEach(entry => {

                        if (entry.isIntersecting) {

                            entry.target
                                .classList
                                .add("is-visible");

                            obs.unobserve(
                                entry.target
                            );

                        }

                    });

                },

                {
                    threshold: 0.12
                }

            );


        elementos.forEach(elemento => {

            observer.observe(elemento);

        });

    } else {

        elementos.forEach(elemento => {

            elemento.classList.add(
                "is-visible"
            );

        });

    }


    /* =========================================
       GALERÍA AUTOMÁTICA
       
       CAMBIA CADA 4 SEGUNDOS
    ========================================= */

    const galeria =
        document.getElementById(
            "galleryCarousel"
        );


    if (galeria) {

        const carousel =
            bootstrap.Carousel
            .getOrCreateInstance(
                galeria,
                {

                    interval: 4000,

                    ride: "carousel",

                    pause: "hover",

                    touch: true,

                    wrap: true

                }
            );


        /* =====================================
           MINIATURAS DE GALERÍA
        ===================================== */

        const miniaturas =
            document.querySelectorAll(
                ".gallery-thumb"
            );


        miniaturas.forEach(miniatura => {

            miniatura.addEventListener(
                "click",
                () => {

                    const indice =
                        Number(
                            miniatura.dataset
                            .galleryIndex
                        );


                    carousel.to(indice);


                    galeria.scrollIntoView({

                        behavior: "smooth",

                        block: "center"

                    });

                }
            );

        });

    }


    /* =========================================
       EFECTO DE PRESIÓN DE BOTONES
    ========================================= */

    const botones =
        document.querySelectorAll(
            ".btn, .nav-link, .gallery-thumb"
        );


    botones.forEach(boton => {

        boton.addEventListener(
            "pointerdown",
            () => {

                boton.classList.add(
                    "pressed"
                );

            }
        );


        boton.addEventListener(
            "pointerup",
            () => {

                boton.classList.remove(
                    "pressed"
                );

            }
        );


        boton.addEventListener(
            "pointerleave",
            () => {

                boton.classList.remove(
                    "pressed"
                );

            }
        );

    });

});


/* =========================================
   CONTACTO → WHATSAPP
========================================= */

function abrirWhatsApp(event) {

    event.preventDefault();


    const nombre =
        document.getElementById(
            "nombre"
        ).value.trim();


    const correo =
        document.getElementById(
            "correo"
        ).value.trim();


    const mensaje =
        document.getElementById(
            "mensaje"
        ).value.trim();


    const texto =

        "Hola ASOPROMUVI. " +

        "Mi nombre es " +
        nombre +

        ". Mi correo es " +
        correo +

        ". Mensaje: " +
        mensaje;


    window.open(

        "https://wa.me/573142552654?text=" +

        encodeURIComponent(texto),

        "_blank"

    );


    return false;

}
