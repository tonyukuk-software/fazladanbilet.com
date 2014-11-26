jQuery(function ($) {
    $('.fancybox').fancybox({
        openEffect: 'elastic',
        closeEffect: 'elastic',
        maxWidth: 890,
        maxHeight: 510,
        autoSize: true,
        minWidth: 280,
        margin: 10,
        padding: [8, 8, 53, 8],
        tpl: {
            wrap: '<div class="fancybox-wrap" tabIndex="-1"><div class="fancybox-wrap-popup fancybox-skin"><div class="fancybox-outer"><div class="fancybox-inner"></div></div></div></div>',
            next     : '<a title="Next" class="fancybox-wrap-popup-next" href="javascript:;"><span></span></a>',
            prev     : '<a title="Previous" class="fancybox-wrap-popup-prev" href="javascript:;"><span></span></a>',
            closeBtn : '<a title="Close" class="fancybox-wrap-popup-close" href="javascript:;"></a>'
        },
        helpers: {
            title: {
                type: 'inside'
            }
        }
    });
});