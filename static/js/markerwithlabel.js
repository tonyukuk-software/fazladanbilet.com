// Define the overlay, derived from google.maps.OverlayView
function MarkerLabel(opt_options) {

    opt_options = opt_options || {};
    opt_options.labelClass = opt_options.labelClass || "";
    opt_options.labelText = opt_options.labelText || "";

    // Initialization
    this.setValues(opt_options);

    // MarkerLabel specific
    var span = this.span_ = document.createElement('span');
    span.className = opt_options.labelClass;
    this.span_.innerHTML = opt_options.labelText;

    var div = this.div_ = document.createElement('div');
    div.appendChild(span);
    div.style.cssText = 'position: absolute; display: none';

    this.isHidden = false;
}
MarkerLabel.prototype = new google.maps.OverlayView;

// Implement onAdd
MarkerLabel.prototype.onAdd = function() {
    var pane = this.getPanes().overlayImage;
    pane.appendChild(this.div_);

    // Ensures the label is redrawn if the text or position is changed.
    var me = this;
    this.listeners_ = [
        google.maps.event.addListener(this, 'position_changed', function() { me.draw(); }),
        google.maps.event.addListener(this, 'visible_changed', function() { me.draw(); }),
        google.maps.event.addListener(this, 'clickable_changed', function() { me.draw(); }),
        google.maps.event.addListener(this, 'text_changed', function() { me.draw(); }),
        google.maps.event.addListener(this, 'zindex_changed', function() { me.draw(); }),
        google.maps.event.addDomListener(this.div_, 'click', function() {
            if (me.get('clickable')) {
                google.maps.event.trigger(me, 'click');
            }
        })
    ];
};

// Implement onRemove
MarkerLabel.prototype.onRemove = function() {
    this.div_.parentNode.removeChild(this.div_);

    // MarkerLabel is removed from the map, stop updating its position/text.
    for (var i = 0, I = this.listeners_.length; i < I; ++i) {
        google.maps.event.removeListener(this.listeners_[i]);
    }
};

// Implement draw
MarkerLabel.prototype.draw = function() {
    var projection = this.getProjection();
    var position = projection.fromLatLngToDivPixel(this.get('position'));

    var div = this.div_;
    div.style.left = position.x + 'px';
    div.style.top = position.y + 'px';
    div.style.display = this.isHidden ? 'none' : 'block';
};