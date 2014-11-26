jQuery(function ($) {

    if (window.innerWidth > BREAK.LG) {
        $(window).on('scroll', function () {
            $('[data-fixed_top]').each(function () {
                var elementParent = $(this).parent('.is-fixed-container'),
                    elementOffsetTop = elementParent.offset().top,
                    elementStatus = ($(this).hasClass('is-fixed-element')) ? true : false;
                var elementHeight = $(this).outerHeight();
                if ($(window).scrollTop() >= elementOffsetTop && !elementStatus) {
                    elementStatus = true;
                    $(this).addClass('is-fixed-element');
                    elementParent.css('height', elementHeight);
                } else if ($(window).scrollTop() < elementOffsetTop && elementStatus) {
                    $(this).removeClass('is-fixed-element');
                    elementParent.css('height', 'auto');
                }
            })
        })
    }
});