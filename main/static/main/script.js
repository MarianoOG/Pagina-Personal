$(document).ready(function() {
    var path = window.location.pathname;

    if(path === '/' || path === '/en'){

        var href = document.location.href
        var origin = document.location.origin
        var res = href.replace(origin, "").substring(1);

        if(res!=='') {
            $('html, body').animate({
                scrollTop: $(res).offset().top - 50
            }, 10);
        }

        $(".nav-offset").click(function(e) {
            e.preventDefault();
            var href = $(this).attr('href').substring(1);
            console.log(href)
            $('html, body').animate({
                scrollTop: $(href).offset().top - 50
            }, 1000);
        });

    } else {

        $(".nav-offset").click(function(e) {
            e.preventDefault();
            var href = $(this).attr('href').substring(1);
            console.log(href)
            window.location.href = document.location.origin + href;
        });

    }
});