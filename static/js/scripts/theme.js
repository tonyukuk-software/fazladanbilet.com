jQuery.noConflict();
jQuery(document).ready(function()
	{

		/*--------------------------------------------*/
		/*- RESPONSIVE -------------------------------*/
		/*--------------------------------------------*/
		jQuery("#menu-drop-button").bind("click", function(){
			jQuery("#nav").slideToggle();
			return false;
		});

		/*--------------------------------------------*/
		/*- FITVID -----------------------------------*/
		/*--------------------------------------------*/

		jQuery(".fitvid").fitVids();


		/*--------------------------------------------*/
		/*- VIDEO WIDGET -----------------------------*/
		/*--------------------------------------------*/

		jQuery(".latest-videos .content").css({"left": 0});
		jQuery(".video-slider-buttons .next, .video-slider-buttons .previous").click(function(){

			var slidingelement = jQuery(this).parent().parent().children(".content");
			var left = slidingelement.css("left").replace("px", "");
			var frame = -Math.round(left/240);
			var vidmax = (slidingelement.children("div").size()-1);

			if(jQuery(this).hasClass("next")){
				i = +frame+1;
			} else {
				i = +frame-1;
			}

			if(jQuery(this).hasClass("next") && vidmax < i) {
				i = 0;
			} else if(jQuery(this).hasClass("previous") && i < 0) {
				i = vidmax;
			}

			newleft = (i*(-240))+"px";
			slidingelement.animate({"left": newleft},{duration: 500});
			return false;
		});


		/*--------------------------------------------*/
		/*- TEAM JQUERY ------------------------------*/
		/*--------------------------------------------*/
		jQuery(".team-member").hover(function () {jQuery(this).find(".description").slideDown("fast");}, function() {jQuery(this).find(".description").slideUp("fast");});

		/*--------------------------------------------*/
		/*- FEATURES ---------------------------------*/
		/*--------------------------------------------*/

		jQuery(".features-title-list li").click(function(){
			oldli = jQuery(".active").index();
			newli = jQuery(this).index();
			jQuery(".active").removeClass("active");
			jQuery(this).addClass("active");

			jQuery("#left-column ul").children("li").eq(oldli).slideUp({duration: 500});
			jQuery("#left-column ul").children("li").eq(newli).slideDown({duration: 500});
			return false;
		});

		/*--------------------------------------------*/
		/*- TESTIMONIALS JQUERY ----------------------*/
		/*--------------------------------------------*/
		jQuery(".testimonials-content-widget .auto-slide").each(function(){
			var parent = jQuery(this).parent().children(".testimonials-container");
			var interval = (jQuery(this).text()*1000);

			if(jQuery(this).text() == '' || jQuery(this).text() == 0)
				return false;

			testimonial_slide = setInterval(function(){
				var current = parent.children(".testimonial-item.active").index();
				var max = parent.children(".testimonial-item").size();
				if(max > 1) {
					var next = (current+1);
					if(max == next){ var next = 0; }
					parent.children(".testimonial-item.active").slideUp().removeClass("active");
					parent.children(".testimonial-item").eq(next).slideDown().addClass("active");
				}
			}, interval);
		});

		/*--------------------------------------------*/
		/*- BACK TO TOP ------------------------------*/
		/*--------------------------------------------*/
		jQuery("#back-top").hide();

		jQuery(window).scroll(function () {
			if (jQuery(this).scrollTop() > 300) {
				jQuery('#back-top').fadeIn();
			} else {
				jQuery('#back-top').fadeOut();
			}
		});

		// scroll body to 0px on click
		jQuery('#back-top a').click(function () {
			jQuery('body,html').animate({
				scrollTop: 0
			}, 800);
			return false;
		});

		/*--------------------------------------------*/
		/*- HEADER CART ------------------------------*/
		/*--------------------------------------------*/
		jQuery(document).on( 'click', ".header-cart-button", function(){
			jQuery(".header-cart").slideToggle("fast");
			jQuery(this).toggleClass("active"); return false;
		});

		/*--------------------------------------------*/
		/*- HEADER CART REFRESH ----------------------*/
		/*--------------------------------------------*/
		jQuery(".add_to_cart_button").bind("click", function(){
			if(jQuery(this).hasClass("product_type_variable")) {
				return true;
			} else {
				setTimeout(function(){
					// Perform the "Magic" which is just a bit of Ajax
					Screen.animate( {scrollTop: 0} );
					jQuery.get(post_page,
						{action : 'ocmx_cart_display'},
						function(data) {
							jQuery("#header-cart").replaceWith( data );
						});

				}, 500);
			}
		});


		/*--------------------------------------------*/
		/*- HEADER SEARCH ----------------------------*/
		/*--------------------------------------------*/


		jQuery("span.icon-search").bind("click", function(e){
			jQuery("#header-contacts").toggleClass("active");
			jQuery("body").toggleClass("search-open");
			e.stopPropagation();
		});

		jQuery( ".search_button, #s" ).bind("click", function(e){
			e.stopPropagation();
		});

		jQuery("body").bind("click", function(){
			if( jQuery( "body" ).hasClass("search-open") ){
				jQuery("#header-contacts").removeClass("active");
				jQuery("body").removeClass("search-open");
			}
		});

		/*--------------------------------------------*/
		/*- EQUAL HEIGHT JQUERY ----------------------*/
		/*--------------------------------------------*/

 		 fix_heights(jQuery('.content-widget-item.post .column .content'));
 		 fix_heights(jQuery('.content-widget-item.portfolio .column .content'));
		 fix_heights(jQuery('#home_page_three_column').find('.content'));


		 /*--------------------------------------------*/
		/*- ADD HEADER PADDING - WIDE LAYOUT --------*/
		/*--------------------------------------------*/
		jQuery(window).resize(function () {
			pad_content_container();
		});
		pad_content_container();
	}); // document.ready

function pad_content_container() {
	var currentHeight = jQuery('#header-container').height();
	if (jQuery(window).width() > 768) {
		jQuery('#content-container').css('padding-top',currentHeight);
	} else {
		jQuery('#content-container').css('padding-top', 0);
	}
} // pad_content_container


function fix_heights($selector) {
	var tallest = 0,
	    elements = new Array(),
	    $el;

	$selector.each(function() {
		$el = jQuery(this);
		elements.push($el);
		tallest = (tallest < $el.height()) ? $el.height() : tallest;
	}); // for each selector

   for (i = 0; i < elements.length; i++) {
       elements[i].css({'minHeight': tallest});
   } // for each element
} // fix_heights
