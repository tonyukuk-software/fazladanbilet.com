jQuery(function ($) {
    var activeTab = 1;
    // Jquery UI Tabs
    $('.j-tabs').tabs();

    // Vertical tabs
    $('.j-tabs-vertical').each(function () {
        var vtabs = $(this);
        if (vtabs.attr('data-active')) {
            activeTab = vtabs.attr('data-active');
        } else {
            activeTab = 1;
        }
        vtabs.tabs({active: activeTab - 1}).addClass("ui-tabs-vertical ui-helper-clearfix");
        vtabs.find('li').removeClass("ui-corner-top").addClass("ui-corner-left");
    });

    // Jquery UI accordion
    $(".j-accordion").accordion({
        heightStyle: "content",
        collapsible: true
    });

    // Bootstrap Tooltip
    $('.j-tooltip').tooltip().on('click', function (e) {
        $(this).tooltip('toggle');
    });

    // Jquery UI Datepicker
    $(".datepicker").datepicker();

});
