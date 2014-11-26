var $bxsliderPrimary, $bxsliderCarousel, $bxsliderCarousel2, $bxsliderImages, $bxsliderInCarousel;
var bxsliderArray = [];

var sliderSettings = {
    mode: 'fade',
    auto: true,
    pager: false
};

var carouselSettings = {
    controls: true,
    maxSlides: 3,
    minSlides: 1,
    moveSlides: 2,
    pager: false,
    slideMargin: 0,
    nextText: '',
    prevText: ''
};

jQuery(function ($) {

    $bxsliderPrimary = $('.j-slider-primary').bxSlider($.extend({}, sliderSettings, {
        controls: false,
        pager: true
    }));

    $bxsliderCarousel = $('.j-carousel-primary').bxSlider($.extend({}, carouselSettings, {
        controls: false,
        slideMargin: 30,
        slideWidth: 568,
        pager: true
    }));

    $bxsliderCarousel2 = $('.j-carousel-secondary').bxSlider($.extend({}, carouselSettings, {
        slideMargin: 28,
        slideWidth: 370
    }));

    $bxsliderCarousel2 = $('.j-carousel-sidebar').bxSlider($.extend({}, carouselSettings, {
        slideMargin: 28,
        slideWidth: 270
    }));

    logoSlider();

    $bxsliderImages = $('.j-slider-images').bxSlider($.extend({}, carouselSettings, {
        maxSlides: 1,
        moveSlides: 1
    }));

    $bxsliderInCarousel = $('.j-slider-in-carousel').bxSlider($.extend({}, carouselSettings, {
        maxSlides: 1,
        moveSlides: 1,
        pager: true
    }));

    function logoSlider() {
        $('.j-logo-slider:visible').each(function () {
            var slider = $(this);
            slider.bxSlider($.extend({}, carouselSettings, {
                auto: true,
                maxSlides: 5,
                moveSlides: 3,
                slideWidth: 208
            }));
        });
    }

    bxsliderArray.push($bxsliderPrimary, $bxsliderCarousel, $bxsliderCarousel2, $bxsliderImages, $bxsliderInCarousel);

    function imgPreload($collection, $elEvent){
        var colLenght = $collection.length;
        var counter = 0;
        $collection.each(function(){
            var src = $(this).attr('src');
            var img = new Image();
            img.src = src;
            img.onload = function(){
                counter++;
                if(counter >= colLenght){
                    $elEvent.trigger('imgsLoaded');
                    return false;
                }
            };
        });
    }

    if ($('.slider-carousel-roundabout').length) {
        var $carouselData = $('.carousel-roundabout-data');
        imgPreload($('.roundabout-slide').find('img'), $('.slider-carousel-roundabout'));
        var curSize;
        $('.slider-carousel-roundabout').on('imgsLoaded', function(){
            $carouselData.css('display', 'none');
            $carouselData.clone()
                .prependTo('.b-carousel-roundabout-wrap')
                .removeClass('carousel-roundabout-data')
                .addClass('b-carousel-roundabout')
                .css('display', 'block');
            $(window).on('resize', function () {
                windowSize();
            });
            reloadSlider();
        });

        function reloadSlider() {
            $('.b-carousel-roundabout').remove();
            $carouselData.clone()
                .prependTo('.b-carousel-roundabout-wrap')
                .removeClass('carousel-roundabout-data')
                .addClass('b-carousel-roundabout')
                .css('display', 'block');
            carouselInit();
        }

        function windowSize() {
            if ($(window).width() > 768 && curSize != 'desktop') {
                reloadSlider();
                curSize = 'desktop';
            }
            else if ($(window).width() > 480 && $(window).width() <= 768 && curSize != 'tablet') {
                reloadSlider();
                curSize = 'tablet';
            } else if ($(window).width() <= 480 && curSize != 'mobile') {
                reloadSlider();
                curSize = 'mobile';
            }
        }

        function carouselInit() {
            setTimeout(function () {
                var $carou = $('.b-carousel-roundabout');
                $carou.roundabout({
                    childSelector: ".roundabout-slide",
                    minOpacity: 1,
                    autoplay: true,
                    autoplayDuration: 4166,
                    autoplayPauseOnHover: true,
                    tilt: 5,
                    minScale: 0.1,
                    reflect: false
                });
                $carou.roundabout('animateToNextChild');
            }, 50);
        }

    }
});
