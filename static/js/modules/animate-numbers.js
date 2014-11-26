jQuery(function ($) {
    // Video - numbers animate
    $('.j-number-up-wrap').on('scrollSpy:enter', function () {
        if (!$(this).hasClass('is-completed')) {
            $(this).addClass('is-completed');
            $('.j-number-up').each(function (i) {
                var INCSTEP = 100;
                var number = 0,
                    $self = $(this),
                    inc;
                var videoNumberStr = $(this).html();
                var videoNumber = parseInt(videoNumberStr, 10);
                inc = videoNumber / INCSTEP;
                NumberUp();

                function NumberUp() {
                    number += inc;
                    if (number <= videoNumber) {
                        $self.html(Math.ceil(number));
                        setTimeout(NumberUp, 5);
                    }
                }
            });
        }
    });
    $('.j-number-up-wrap').scrollSpy();
});