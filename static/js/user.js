jQuery(function ($) {

    // + fb widget
    function fbWidget(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) {
            return;
        }
        js = d.createElement(s);
        js.id = id;
        js.src = "//connect.facebook.net/en_EN/sdk.js#xfbml=1&version=v2.0";
        fjs.parentNode.insertBefore(js, fjs);
    }

    if ($('#fb-root').size() > 0) {
        fbWidget(document, 'script', 'facebook-jssdk');
    }
    // - fb widget


    var dropDownMenu = {
        mobileMenuContainer: '.j-menu-container',
        dropMenuVisible: false,
        init: function () {
            this.showHideMenu();
            this.resize();
        },
        showHideMenu: function () {
            var self = this;
            $('.j-top-nav-show-slide').on('click', function () {
                var $cloneNav = $('.j-menu-container .j-top-nav');
                if (!self.dropMenuVisible) {
                    $('.j-top-nav').clone().prependTo(self.mobileMenuContainer).addClass('b-top-nav-dropdown').addClass('f-top-nav-dropdown').animate({height: "toggle"}, 700);
                    self.dropMenuVisible = true;
                } else {
                    $cloneNav.animate({height: "toggle"}, 700, function () {
                        $cloneNav.remove();
                    });
                    self.dropMenuVisible = false;
                }
                self.toggleIcon();
            });
        },
        toggleIcon: function () {
            var self = this;
            $(self.mobileMenuContainer + ' .b-ico-dropdown').on('click', function () {
                var $liFirstLevel = $(this).parents('.b-top-nav__1level');
                $liFirstLevel.toggleClass('is-active-top-nav__dropdown');
                $liFirstLevel.find('.fa').toggleClass('fa-arrow-circle-down').toggleClass('fa-arrow-circle-up');
                $liFirstLevel.find('.b-top-nav__dropdomn').slideToggle('slow');
                return false;
            });
        },
        resize: function () {
            var self = this;
            $(window).on('resize', function () {
                if ($(self.mobileMenuContainer + ' .j-top-nav') && self.dropMenuVisible && $(window).width() > BREAK.MD) {
                    $('.j-top-nav-show-slide').click();
                    self.dropMenuVisible = false;
                }
            });
        }
    };
    dropDownMenu.init();

    var pageDecoration = {
        groupAnimatecontroller: true,
        groupAnimateSize: 0,
        init: function () {
            var self = this;
            self.galleryHoverInfo();
            self.animateCategoryIcons();
            self.fadeInAnimation();
            self.imagesAppearance();
            self.toHeightScreen($('.slider-carousel-roundabout'));
            self.toHeightScreen($('.slider-video-container'), 92);
            self.hoverDependence($('.b-blog-short-post__item_img a'), $('.b-blog-short-post__item_text a'), $('.b-blog-short-post__item'));
            self.togleActive();
        },
        galleryHoverInfo: function () {
            $('.j-item-hover-action').hover(function () {
                $(this).find('.b-item-hover-action, [class*="b-item-hover-action--"]').addClass('is-visible fadeIn animated');
            }, function () {
                $(this).find('.b-item-hover-action, [class*="b-item-hover-action--"]').removeClass('is-visible fadeIn animated');
            });
        },
        animateCategoryIcons: function () {
            $('.b-categories-icons__item').hover(function () {
                $(this).addClass('is-active-categories-icons__item');
            }, function () {
                $(this).removeClass('is-active-categories-icons__item');
            });
        },
        fadeInAnimation: function () {
            var self = this;
            $('.fade-in-animate').on('scrollSpy:enter', function () {
                var el = $(this);
                if (el.attr('data-animate-group')) {
                    el.addClass('group-animate');
                }
                if ((el.attr('data-animate-group')) && ( self.groupAnimatecontroller)) {
                    self.groupAnimatecontroller = false;
                    setTimeout(function () {
                        self.groupAnimateSize = $('.group-animate').size();
                        self.fadeInGroup();
                        self.groupAnimatecontroller = true;
                    }, 100);
                } else if (!(el.attr('data-animate-group'))) {
                    el.addClass('visible');
                }
            }).scrollSpy();
            $('.j-data-element').on('scrollSpy:enter', function () {
                var animateType = $(this).data('animate');
                $(this).addClass('animated ' + animateType);
            }).scrollSpy();
        },
        fadeInGroup: function () {
            var self = this;
            self.groupAnimateSize--;
            $('body').find('.group-animate').eq(0).addClass('visible').removeClass('group-animate').removeAttr('data-animate-group');
            if (self.groupAnimateSize > 0) {
                setTimeout(self.fadeInGroup, 300);
            }
        },
        imagesAppearance: function () {
            $('.wrap-img-appearance').on('scrollSpy:enter', function () {
                var $elements = $(this).find('img');
                var index = 0;

                function eachEl() {
                    var animateType = $elements.eq(index).data('animate');
                    $elements.eq(index).addClass('animated').addClass(animateType);
                    index++;
                    if (index >= $elements.length) {
                        clearTimeout(time);
                    }
                }

                var time = setInterval(eachEl, 250);
            }).scrollSpy();
        },
        setElHeight: function (height, $el, k) {
            if (k) {
                $el.css('height', height - k);
            }
            else {
                $el.css('height', height);
            }
        },
        toHeightScreen: function ($el, k) {
            var self = this;
            if ($el.length) {
                $(window).on('resize', function () {
                    self.setElHeight($(window).outerHeight(), $el, k);
                });
                self.setElHeight($(window).outerHeight(), $el, k);
            }
        },
        hoverDependence: function (el1, el2, parent) {
            el1.hover(function () {
                    $(this).closest(parent).find(el2).addClass('is-hover');
                },
                function () {
                    $(this).closest(parent).find(el2).removeClass('is-hover');
                });
            el2.hover(function () {
                    $(this).closest(parent).find(el1).addClass('is-hover');
                },
                function () {
                    $(this).closest(parent).find(el1).removeClass('is-hover');
                });
        },
        togleActive: function () {
            $('.j-toggle-active').on('click', function (e) {
                e.preventDefault();
                $(this).toggleClass('is-active');
            });
        }
    };
    pageDecoration.init();

    var revolutionSlider = {
        islider: $('.j-fullscreenslider, .j-contentwidthslider, .j-smallslider'),
        init: function () {
            var self = this;
            self.revSliderInit();
            self.islider.on('rerenderRevSlider', function () {
                self.rerenderSlider();
            });
        },
        revSliderInit: function () {
            var revapi,
                self = this;

            this.islider.each(function () {
                var slider = $(this);
                var args = {
                    delay: 6300,
                    startwidth: 1170,
                    startheight: 500,
                    hideThumbs: 10,
                    navigationArrows: "solo"
                };
                if (slider.hasClass('j-smallslider')) {
                    args.startwidth = "560";
                    args.startheight = "330";
                    args.navigationType = "none";
                    args.navigationStyle = "square";
                }
                if (slider.hasClass('j-contentwidthslider')) {
                    args.startwidth = "1170";
                }
                if (slider.hasClass('j-contentwidthslider-innerheight')) {
                    args.startheight = "316";
                }
                if (slider.hasClass('j-arr-nexttobullets')) {
                    args.navigationArrows = "nexttobullets";
                }
                if (slider.hasClass('j-arr-hide')) {
                    args.navigationArrows = "none";
                }
                if (slider.hasClass('b-video-slider')) {
                    args.navigationVOffset = 153;
                    args.autoHeight = 'on';
                    args.startheight = 1024;
                }
                if (slider.hasClass('j-pagination-hide')) {
                    args.navigationType = "none";
                }
                if (slider.attr('data-height')) {
                    args.startheight = slider.data('height');
                }
                if (slider.attr('data-thumb-amount')) {
                    args.navigationType = "thumb";
                    args.thumbAmount = slider.data('thumb-amount');
                    args.thumbWidth = 176;
                    args.thumbHeight = 105;
                    args.hideThumbs = 0;
                    delete args.startwidth;
                    delete args.startheight;
                }
                if (slider.closest('.b-slider').hasClass('b-slider--thumb')) {
                    var mass = [];
                    var img = slider.find('img');
                    img.each(function () {
                        mass.push($(this).attr('src'));
                    });
                    revapi = slider.revolution(args);
                    self.islider.bind('revolution.slide.onloaded', function () {
                        slider.next('.tp-bullets').find('.bullet').each(function (i) {
                            $(this).css('background', 'url(' + mass[i] + ') no-repeat scroll 0px 0px / cover transparent');
                        });
                        self.islider.unbind('revolution.slide.onloaded');
                    });
                } else {
                    revapi = slider.revolution(args);
                }
            });
        },
        rerenderSlider: function () {
            var self = this;
            self.islider.revnext();
            setTimeout(function () {
                self.islider.revnext();
            }, 2000);
        }
    };
    revolutionSlider.init();

    var backgroundVideo = {
        init: function () {
            var self = this;
            if ((navigator.userAgent.match(/iPhone/i)) ||
                (navigator.userAgent.match(/iPad/i)) ||
                (navigator.userAgent.match(/iPod/i))) {
                $('.b-bg-video').addClass('device-ios');
            }
            self.videoControls();
            self.videoScrollSpy();
        },
        videoControls: function () {
            $('.j-video-controls i').on('click', function () {
                var video = $("#video1")[0];
                if (video.paused) {
                    video.play();
                } else {
                    video.pause();
                }
                $(this).hide().siblings().css('display', 'inline-block');
            });
        },
        videoScrollSpy: function () {
            var $video1 = $('#video1');

            $video1.on('scrollSpy:enter', function () {
                if ($(this)[0].paused) {
                    $(this)[0].play();
                }
                $('#video1-play').hide();
                $('#video1-pause').show();
            });

            $video1.on('scrollSpy:exit', function () {
                $(this)[0].pause();
                $('#video1-play').show();
                $('#video1-pause').hide();
            });

            $video1.scrollSpy();
        }

    };
    backgroundVideo.init();

    var formEls = {
        init: function () {
            var self = this;
            self.select();
            self.sliderRange();
            self.inputFile();
            self.placeholder();
            self.inputNumber();
            self.inputNumberMore();
            self.inputNumberLess();
            $(window).on('resize', function () {
                self.resize();
            });

        },
        select: function () {
            $(".j-select").each(function () {
                $(this).selectmenu({
                    width: $(this).css('width'),
                    disabled: $(this).prop('disabled')
                });
            });
        },
        sliderRange: function () {
            $(".j-slider-range").each(function () {
                var rangeSlider = $(this);
                rangeSlider.slider({
                    range: true,
                    min: 0,
                    max: 999,
                    values: [ 200, 700 ],
                    slide: function (event, ui) {
                        rangeSlider.find('.max').text("$" + ui.values[ 1 ]);
                        rangeSlider.find('.min').text("$" + ui.values[ 0 ]);
                    }
                });
                var handle = rangeSlider.find('.ui-slider-handle');
                handle.filter(':first').append('<span class="min"></span>');
                handle.filter(':last').append('<span class="max"></span>');
                handle.find('.min').text("$" + rangeSlider.slider("values", 0));
                handle.find('.max').text("$" + rangeSlider.slider("values", 1));
            });
        },
        inputFile: function () {
            var wrapper = $(".file_upload"),
                inp = wrapper.find("input"),
                btn = wrapper.find("button"),
                lbl = wrapper.find("div");

            btn.focus(function () {
                inp.focus()
            });
            // Crutches for the :focus style:
            inp.focus(function () {
                wrapper.addClass("focus");
            }).blur(function () {
                wrapper.removeClass("focus");
            });

            var file_api = ( window.File && window.FileReader && window.FileList && window.Blob ) ? true : false;

            inp.change(function () {
                var file_name;
                if (file_api && inp[ 0 ].files[ 0 ])
                    file_name = inp[ 0 ].files[ 0 ].name;
                else
                    file_name = inp.val().replace("C:\\fakepath\\", '');

                if (!file_name.length)
                    return;

                if (lbl.is(":visible")) {
                    lbl.text(file_name);
                } else
                    btn.text(file_name);
            }).change();
        },
        placeholder: function () {
            $('input, textarea').placeholder();
        },
        inputNumber: function () {
            $('input[type=number]').each(function () {
                var el = $(this);
                $('<div class="input-number-box"></div>').insertAfter(el);
                var parent = el.find('+ .input-number-box');
                parent.append(el);
                var classes = el.attr('class');
                parent.append('<input class="input-number" type="text">');
                el.hide();
                var newEl = el.next();
                newEl.addClass(classes);
                var attrValue;

                function setInputAttr(attrName) {
                    if (el.attr(attrName)) {
                        attrValue = el.attr(attrName);
                        newEl.attr(attrName, attrValue);
                    }
                }

                setInputAttr('value');
                setInputAttr('placeholder');
                setInputAttr('min');
                setInputAttr('max');
                setInputAttr('step');

                parent.append('<div class="input-number-more"></div>');
                parent.append('<div class="input-number-less"></div>');
            });

        },
        inputNumberMore: function () {
            $('body').on('click', '.input-number-more', function () {
                var el = $(this);
                var input = el.closest('.input-number-box').find('.input-number');
                var max = input.attr('max');
                var value;

                if (input.attr('value')) {
                    value = parseFloat(input.attr('value'));
                } else if (input.attr('placeholder')) {
                    value = parseFloat(input.attr('placeholder'));
                }
                if (!( $.isNumeric(value) )) {
                    value = 0;
                }

                var step;
                if (input.attr('step')) {
                    step = parseFloat(input.attr('step'));
                } else {
                    step = 1;
                }
                var newValue = value + step;
                if (newValue > max) {
                    newValue = max;
                }
                input.val(newValue);
                var inputNumber = el.closest('.input-number-box').find('[type=number]');
                inputNumber.val(newValue);
            });
        },
        inputNumberLess: function () {
            $('body').on('click', '.input-number-less', function () {
                var el = $(this);
                var input = el.closest('.input-number-box').find('.input-number');
                var min = input.attr('min');
                var value;

                if (input.attr('value')) {
                    value = parseFloat(input.attr('value'));
                } else if (input.attr('placeholder')) {
                    value = parseFloat(input.attr('placeholder'));
                }
                if (!( $.isNumeric(value) )) {
                    value = 0;
                }

                var step;
                if (input.attr('step')) {
                    step = parseFloat(input.attr('step'));
                } else {
                    step = 1;
                }
                var newValue = value - step;
                if (newValue < min) {
                    newValue = min;
                }
                input.val(newValue);
                var inputNumber = el.closest('.input-number-box').find('[type=number]');
                inputNumber.val(newValue);
            });
        },
        resize: function () {
            $(".file_upload input").triggerHandler("change");
        }
    };
    formEls.init();

    var totalPrice = {
        boxEL: ".j-price-count-box",
        counterEL: ".j-product-count",
        parentEL: "tr:not(:first-child)",
        priceEL: ".j-product-price",
        totalEL: ".j-product-total",
        priceTotal: ".j-price-total",
        totalCount: 0,
        init: function () {
            var self = this;
            self.getTotalPrice();
            self.changeCounterEl();
        },
        getTotalPrice: function () {
            var self = this;
            self.totalCount = 0;
            $(self.parentEL).each(function () {
                var el = $(this);
                var currentPrice = parseFloat(el.find(self.priceEL).text()).toFixed(2) * parseFloat(el.find(self.counterEL).val());
                el.find(self.totalEL).text(currentPrice.toFixed(2));
                self.totalCount += currentPrice;
            });
            self.totalPrice(self.totalCount);
        },
        totalPrice: function () {
            var self = this;
            $(self.priceTotal).text(self.tolalCount);
        },
        changeCounterEl: function () {
            var self = this;
            $(self.counterEL).change(function () {
                self.getTotalPrice();
            });
        }
    };
    totalPrice.init();

    var menu = {
        init: function () {
            var self = this;
            self.onHover();
            self.multiLvlMenu();
        },
        onHover: function () {
            $('.b-top-nav__1level').hover(function () {
                if ($(window).width() > (BREAK.MD - 1)) {
                    var dropEL = $(this).find('.b-top-nav__dropdomn');
                    if (dropEL.length !== 0) {
                        var leftPosition = dropEL.offset().left;
                        var rightPosition = dropEL.offset().left + dropEL.outerWidth();

                        if (leftPosition < 0) {
                            dropEL.addClass('nav-position-right');
                        } else {
                            dropEL.removeClass('nav-position-right');
                        }

                        if (rightPosition > $(window).width()) {
                            dropEL.addClass('nav-position-left');
                        } else {
                            dropEL.removeClass('nav-position-left');
                        }
                    }
                }
            });
        },
        multiLvlMenu: function () {
            $('body').on('click', '.b-top-nav__with-multi-lvl', function () {
                if ($(window).width() < (BREAK.MD)) {
                    if ($(this).hasClass('is-active-multi-lvl')) {
                        $(this).removeClass('is-active-multi-lvl');
                        $(this).find(' > .b-top-nav__multi-lvl-box').slideUp();
                    } else {
                        $(this).addClass('is-active-multi-lvl');
                        $(this).find(' > .b-top-nav__multi-lvl-box').slideDown();
                    }
                }
            });
            $('body').on('click', '.b-top-nav__multi-lvl', function (e) {
                e.stopPropagation();
            });
        }

    };
    menu.init();

    var masonryFilter = {
        massMasonry: [],
        dataFilterVal: "all",
        init: function () {
            var self = this;
            self.filterEl('.j-filter', '.j-filter-content');
            self.masonry();
        },
        masonry: function () {
            var self = this;
            var msnry;
            var i = 0;
            $('.j-masonry').each(function () {
                var el = $(this),
                    newClass = 'j-masonry-' + i;

                el.addClass(newClass).attr('data-masonry-id', i);
                i++;
                el.imagesLoaded(function () {
                    var container = document.querySelector('.' + newClass);

                    msnry = new Masonry(container,
                        {
                            itemSelector: '.j-masonry-item',
                            columnWidth: '.' + newClass + ' .masonry-gridSizer',
                            transitionDuration: '1.2s'
                        });
                    self.massMasonry.push(msnry);
                });
            });
        },
        filterEl: function (filterNav, filterContent) {
            var self = this;
            $(filterNav + ' a').click(function (e) {
                e.preventDefault();
                var el = $(this);
                var activeClass = "is-category-filter-active";
                $(filterNav + ' li').removeClass(activeClass);
                el.closest('li').addClass(activeClass);
                self.dataFilterVal = el.attr('data-filter');
                self.filterStart(self.dataFilterVal, filterContent);
            });
        },
        filterStart: function (dataFilterVal, filterContent) {
            var self = this;
            if (dataFilterVal == "all") {
                $(filterContent + ' [class*="j-filter-"]').show().stop(true, false).animate({
                    opacity: 1
                }, 400);
            } else {
                var hideItems = $(filterContent + ' [class*="j-filter-"]').not(dataFilterVal);
                hideItems.stop(true, false).animate({
                    opacity: 0
                }, 400);
                setTimeout(function () {
                    hideItems.hide();
                }, 301);
                $(filterContent + " " + dataFilterVal).show().stop(true, false).animate({
                    opacity: 1
                }, 400);
            }
            setTimeout(function () {
                var masonryId = $(filterContent).find('.j-masonry').attr('data-masonry-id');
                self.massMasonry[masonryId].layout();
            }, 501);
        }
    };
    masonryFilter.init();

    var carouFredSelTabs = {
        init: function () {
            var self = this;
            self.paramsInit();
            self.carouFredSelcheckElements();
            $(window).on('resize', function () {
                self.resize();
            });
        },
        paramsInit: function () {
            $('.j-tabs-check-size').carouFredSel({
                auto: {
                    play: false
                },
                prev: '.j-tabs-btn-prev',
                next: '.j-tabs-btn-next',
                items: 'variable',
                mousewheel: true,
                responsive: false,
                infinite: true,
                circular: true,
                swipe: {
                    onMouse: true,
                    onTouch: true
                },
                align: "left",
                width: "100%",
                scroll: {
                    items: 1
                }
            });
        },
        carouFredSelcheckElements: function () {
            var alltabs = $('.j-tabs-check-size > li').length;
            var visibleTabs = $('.j-tabs-check-size').triggerHandler("currentVisible").length;
            if (visibleTabs < alltabs) {
                $('.tabs-wrap').addClass('btns-indent');
                $('.j-tabs-check-size').trigger("updateSizes");
            } else {
                $('.tabs-wrap').removeClass('btns-indent');
            }
        },
        resize: function () {
            this.carouFredSelcheckElements();
        }
    };
    if ($('.j-tabs-check-size').length) {
        carouFredSelTabs.init();
    }

    var headerAndTopButtonPosition = {
        $header: $('header'),
        headerBreakHeight: 0,
        $slider: $('.j-fixed-slider'),
        scrollController: true,
        headerFixed: false,
        toTopBtn: $('.j-footer__btn_up'),
        windowScrollTop: $(window).scrollTop(),
        init: function () {
            var self = this;
            self.headerBreakHeight = this.$header.offset().top;
            self.checkHeaderWindowWidth();
            self.btnToTopInit();
            $(window).on('resize', function () {
                self.resize();
            });
        },
        checkHeaderWindowWidth: function () {
            var self = this;
            self.headerFixed = false;
            self.windowScrollTop = $(window).scrollTop();
            if (self.$header.length !== 0) {
                self.checkHeaderWindowWidthNow();
                $(window).on('scroll', function () {
                    self.checkHeaderWindowWidthNow();
                });
            }
        },
        checkHeaderWindowWidthNow: function () {
            var self = this;
            if (window.innerWidth > BREAK.LG) {
                self.windowScrollTop = $(window).scrollTop();
                self.checkHeaderPosition();
                self.btnToTop();
            } else {
                $('body').removeClass('is-fixed-header');
                self.$header.removeClass('animated fadeInDown');
            }
        },
        checkHeaderPosition: function () {
            var self = this;
            if (self.windowScrollTop > self.headerBreakHeight && !self.headerFixed) {
                $('body').addClass('is-fixed-header');
                self.$header.addClass('animated fadeInDown');
                self.$slider.addClass('is-active').css('top', self.$header.outerHeight() + 'px');
                self.headerFixed = true;
            }
            else if (self.windowScrollTop <= self.headerBreakHeight && self.headerFixed) {
                $('body').removeClass('is-fixed-header');
                self.$header.removeClass('animated fadeInDown');
                self.$slider.removeClass('is-active');
                self.headerFixed = false;
            }
        },
        btnToTopInit: function () {
            var self = this;
            var SPEEDTOP = 500; // button to top
            self.toTopBtn.addClass('b-hidden').css('opacity', 0);
            self.toTopBtn.css('position', 'fixed');
            self.toTopBtn.on('click', function () {
                var offset = $('body').offset();
                if (offset) {
                    $('html,body').animate({scrollTop: offset.top}, SPEEDTOP);
                }
            });
        },
        btnToTop: function () {
            var self = this;
            if (self.windowScrollTop > self.headerBreakHeight && self.scrollController) {
                self.scrollController = false;
                self.toTopBtn.removeClass('b-hidden');
                self.toTopBtn.stop(true, true).animate({
                    opacity: 1
                }, 1000);
            } else if (self.windowScrollTop <= self.headerBreakHeight) {
                self.scrollController = true;
                self.toTopBtn.addClass('b-hidden').css('opacity', 0);
                self.toTopBtn.stop(true, true).animate({
                    opacity: 0
                }, 1000);
            }
        },
        resize: function () {
            this.checkHeaderWindowWidth();
        }
    };
    headerAndTopButtonPosition.init();

    $('[data-type="background"]').each(function(){
        var $bgobj = $(this);
        $(window).on('scroll', function() {
            var yPos = -($(window).scrollTop() / $bgobj.data('speed'));
            var coords = 'center '+ yPos + 'px';
            $bgobj.css({ backgroundPosition: coords });
        });
    });
});


