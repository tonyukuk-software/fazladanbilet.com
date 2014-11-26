jQuery(function ($) {

    var $radialPb = $("[data-radialprogress]");

    $radialPb.on('scrollSpy:enter',function () {
        if (!$(this).hasClass('is-completed')) {
            $(this).addClass('is-completed');
            var idEl = '#' + $(this).attr('id');
            radialProgress($(idEl)[0])
                .diameter($(this).data('diameter'))
                .value($(this).data('value'))
                .duration($(this).data('duration'))
                .delay($(this).data('delay'))
                .progressStyle($(this).data('style'))
                .render();

        }
    }).scrollSpy();

    function stepProgress() {
        var $stepContainer = $(this).siblings('.progress-steps');
        var widthGlobal = 100;
        var $progressbar = $(this);
        var padding = Number($stepContainer.data('padding'));
        var maxStep = $('[data-transitiongoal]', $stepContainer).length;
        var widthLocal = widthGlobal - padding * 2;
        $('[data-transitiongoal]', $stepContainer).each(function (i) {
            var value = Number($(this).data('transitiongoal')),
                position = (padding + widthLocal * value / 100);
            $(this).data('position', position);
            if (padding === 0) {
                if (i == maxStep - 1){
                    $(this).css({'margin-left': '-' + $(this).outerWidth() + 'px'});
                } else if (i != 0){
                    $(this).css({'margin-left': '-' + $(this).outerWidth() / 2 + 'px'});
                }
                $(this).css({'left': position + '%'});
            } else {
                $(this).css({
                    'left': position + '%',
                    'margin-left': '-' + $(this).outerWidth() / 2 + 'px'
                });
            }
            $(this).attr('data-position', position);
        });
        var step = Number($progressbar.data('step'));
        $('li:nth-child(' + step + ')', $stepContainer).addClass('active');
        var progress = Number($('li:nth-child(' + step + ')', $stepContainer).data('position'));
        if (step == maxStep) {
            progress = '100%';
        }
        $progressbar.css('width', progress + '%');
    }

    var pbType = {
        default_pb: {
            display_text: 'center'
        },
        animate_pb: {
            display_text: 'center',
            update: function (current_percentage, $this) {
                $this.parent('.progress-striped').find('.progressbar-back-text').addClass('is-visible').css('left', current_percentage + '%');
            }
        },
        steps_pb: {
            display_text: 'none'
        }
    };

    var $pb = $('[data-progressbar] .progress-bar:not(.progress-bar-loader)');
    $pb.on('scrollSpy:enter',function () {
        var $pbType = $(this).parents('[data-progressbar]').data('progressbar');
        if ($pbType === '') {
            $pbType = 'default_pb'
        }
        else if ($pbType == 'steps_pb') {
            stepProgress.call($(this));
        }

        $(this).addClass('active').progressbar($.extend({}, pbType[$pbType]));
        if($('.j-progress-tab').size()>0){
            $('.j-progress-tab .active .progress-step__dot').click();
        }
    }).scrollSpy();

    // + j-progress-tab

    $('.j-progress-tab').each(function(){
        var el = $(this);
        var i = 0;
        el.find('.progress-step').each(function(){
            var tabMenuEl = $(this);
            tabMenuEl.attr('data-tab-id', i);
            i++;
        });
    });

    $('.j-progress-tab .progress-step__dot').click(function(e){
        e.preventDefault();
        progressTabClick($(this));
        progressTabNavigation($(this));
    });

    function progressTabClick(el){
        var parent = el.closest('.progress-step');
        var box = el.closest('.j-progress-tab');
        box.find('.progress-step').removeClass('active');
        parent.addClass('active');
        var progressbar = box.find('.progress-bar');
        var newposition = parent.attr('data-position');
        progressbar.animate({
            width : newposition + "%"
        }, 100);
        var arrow = box.find('.b-progress-tab-arr');
        arrow.css('left', newposition + "%");
    }

    function progressTabNavigation(el){
        var parent = el.closest('.progress-step');
        elID = parent.attr('data-tab-id');
        var box = el.closest('.j-progress-tab');
        box.find('.b-tab-progress').hide();
        box.find('.b-tab-progress').eq(elID).show();
    }
    // - j-progress-tab

});
