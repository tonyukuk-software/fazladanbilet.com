jQuery(function ($) {

    var btnAddWrapper = $('[data-settings_layout="on"]'),
        btnRemoveWrapper = $('[data-settings_layout="off"]'),
        btnCnangeBackground = $('[data-bg]'),
        btnReset = $('[data-reset]'),
        classAddBg = 'html-bg',
        classAddPattern = 'html-bg-pattern',
        $wrapper = $('body');

    function AddWrapper() {
        btnRemoveWrapper.removeClass('active');
        btnAddWrapper.addClass('active');
        $wrapper.addClass('l-body-boxed');
        ReloadSliders();
    }

    function RemoveWrapper() {
        btnAddWrapper.removeClass('active');
        btnRemoveWrapper.addClass('active');
        $wrapper.removeClass('l-body-boxed');
        ReloadSliders();
    }

    function ResetBg() {
        $('html').removeClass(classAddBg).removeClass(classAddPattern);
    }

    function ReloadSliders() {
        // Reload Bxslider
        for (var i = 0; i < bxsliderArray.length; i++) {
            if (bxsliderArray[i].reloadSlider) {
                bxsliderArray[i].reloadSlider();
            }
        }
var islider = $('.j-fullscreenslider, .j-contentwidthslider, .j-smallslider');
        //Rerender Revolution Slider
        islider.trigger('rerenderRevSlider');
    }

    btnAddWrapper.on('click', function () {
        AddWrapper();
    });

    btnRemoveWrapper.on('click', function () {
        RemoveWrapper();
    });

    btnCnangeBackground.on('click', function () {
        ResetBg();
        if (!$wrapper.hasClass('l-body-boxed')) {
            AddWrapper();
        }
        btnCnangeBackground.removeClass('active');
        $(this).addClass('active');
        var classHtml;
        if ($(this).data('type') == 'pattern') {
            classHtml = classAddPattern;
        } else if ($(this).data('type') == 'img') {
            classHtml = classAddBg;
        }
        $('html').addClass(classHtml).css({'background-image': 'url("' + $(this).data('bg') + '")'});
        return false;
    });

    btnReset.on('click', function () {
        $(this).trigger('resetColors');
        ResetBg();
        RemoveWrapper();
        $('.settings-bg').find('li').removeClass('active');
    });

    $('.settings-label').on('click', function () {
        $(this).parents('.settings-wrap').toggleClass('active');
    })
});