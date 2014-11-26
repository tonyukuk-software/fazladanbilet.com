$(document).ready(function () {
    var $imageColection,
        counterImgTotal,
        counterImg;
    function compareAndStop(){

        if (counterImg === counterImgTotal - 1) {
            $('.l-wrapper').trigger('imagesLoaded');
            setTimeout(function(){
                $('html').removeClass('loader-lock');
                $('.l-wrapper').addClass('animated fadeOut is-hide');
                return false;
            }, 900);

        }
        counterImg++;
    }
    if ($('html').hasClass('loader-lock')) {
        $imageColection = $('img');
        counterImgTotal = $imageColection.length;
        counterImg = 0;
        setTimeout(function () {

            $imageColection.each(function () {
                var img = new Image();
                if (!$(this).attr('src')) {
                    counterImg++;
                    return true;
                }
                img.src = $(this).attr('src');
                try {
                    img.onload = function () {
                        compareAndStop();
                    };
                }
                catch(e){
                    compareAndStop();
                }
            });
        }, 250);
    }

    function getRandomInt(min, max)
    {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }



    var pbParam = {
        display_text: 'center',
        update: function (current_percentage, $this) {
            $this.parent('.progress-striped').find('.progressbar-back-text').addClass('is-visible').css('left', current_percentage + '%');
        }
    };
    var $pb = $('.progress-bar-loader');
    var percentage = 30;
    $pb.attr('data-transitiongoal', percentage).progressbar(pbParam);
    var stopPercentage = getRandomInt(70, 95);

    var intervalUpd = setInterval(function(){
        percentage += getRandomInt(1, 8);
        if(percentage >= stopPercentage){

            clearInterval(intervalUpd);
            $pb.attr('data-transitiongoal', stopPercentage).progressbar(pbParam);
            return;
        }
        $pb.attr('data-transitiongoal', percentage).progressbar(pbParam);
    }, getRandomInt(300, 2000));

    $('.l-wrapper').on('imagesLoaded', function(){
        clearInterval(intervalUpd);
        $pb.attr('data-transitiongoal', 100).progressbar(pbParam);
        $('.l-wrapper').on('imagesLoaded');
    });

});
