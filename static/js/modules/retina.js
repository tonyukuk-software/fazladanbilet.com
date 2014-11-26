jQuery(function ($) {
    // Retina
    function fixedSizeImgRetina() {
        // Removing Width for recalculation when the window is resized
        $(this).removeAttr("width").attr("width", $(this).outerWidth());
    }

    if (window.devicePixelRatio >= 2) {
        $('img[data-retina]').each(function () {
            var retinasrc = $(this).data("retina");
            if (retinasrc != '') {
                fixedSizeImgRetina.call($(this));
                $(this).attr("src", retinasrc);
            }
        });
    }

    $(window).on('resize', function () {
        $('img[data-retina]').each(function () {
            fixedSizeImgRetina.call($(this));
        })
    });
});