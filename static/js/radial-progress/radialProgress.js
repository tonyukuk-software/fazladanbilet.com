function radialProgress(parent) {
    var duration = 1000,
        delay = 0,
        selection,
        diameter = 100,
        label = "",
        fontSize = 10,
        progressStyle = 'filled';


    var value = 0,
        minValue = 0,
        maxValue = 100;

    var currentArc = 0, currentValue = 0;

    var arc = d3.svg.arc()
        .startAngle(0); //just radians

    var arcBgFill = d3.svg.arc()
        .startAngle(0)
        .endAngle(360 * (Math.PI / 180)); //just radians

    var arcBg = d3.svg.arc()
        .startAngle(0)
        .endAngle(360 * (Math.PI / 180)); //just radians


    selection = d3.select(parent);


    function component() {

        selection.each(function (data) {

            // Select the svg element, if it exists.
            var svg = d3.select(this).selectAll("svg").data([data]);

            var enter = svg.enter().append("svg").attr("class", "radial-svg").append("g");

            measure();

            svg.attr("width", diameter)
                .attr("height", diameter);


            var background = enter.append("g").attr("class", "component")
                .attr("cursor", "pointer");

            arc.endAngle(0);

            if (progressStyle === 'filled') {
                background.append("path")
                    .attr("transform", "translate(" + width / 2 + "," + width / 2 + ")")
                    .attr("d", arcBgFill);
            }
            if (progressStyle === 'notFilled') {
                background.append("path")
                    .attr("transform", "translate(" + width / 2 + "," + width / 2 + ")")
                    .attr("d", arcBg).attr("class", "bg-first-layer");
            }


            enter.append("g").attr("class", "arcs");
            var path = svg.select(".arcs").selectAll(".arc").data(data);
            path.enter().append("path")
                .attr("class", "arc")
                .attr("transform", "translate(" + width / 2 + "," + width / 2 + ")")
                .attr("d", arc);

            enter.append("g").attr("class", "labels");
            if (progressStyle === 'filled') {
                var label = svg.select(".labels").selectAll(".label").data(data);
                label.enter().append("text")
                    .attr("class", "label")
                    .attr("y", width / 2 + fontSize / 3)
                    .attr("x", width / 2)
                    .attr("cursor", "pointer")
                    .attr("width", width)
                    .attr('fill', '#fff')
                    .text(function () {
                        return minValue + "%";
                    })
                    .style("font-size", fontSize + "px");
            }

            layout();

            function layout() {

                var ratio = (value - minValue) / (maxValue - minValue);
                var endAngle = Math.min(360 * ratio, 360);
                endAngle = endAngle * Math.PI / 180;

                path.datum(endAngle);
                path.transition().duration(duration).delay(delay)
                    .attrTween("d", arcTween);
                if (progressStyle === 'filled') {
                    label.datum(Math.round(ratio * 100));
                    label.transition().duration(duration).delay(delay)
                        .tween("text", labelTween);
                }

            }

        });
    }

    function labelTween(a) {
        var i = d3.interpolate(currentValue, a);
        currentValue = i(0);

        return function (t) {
            currentValue = i(t);
            this.textContent = Math.round(i(t)) + "%";
        }
    }

    function arcTween(a) {
        var i = d3.interpolate(currentArc, a);
        return function (t) {
            currentArc = i(t);
            return arc.endAngle(i(t))();
        };
    }


    function measure() {
        height = width = diameter;
        fontSize = width * .144;
        arc.outerRadius(width / 2 * .85);
        arc.innerRadius(width / 2 * .76);
        arcBgFill.outerRadius(width / 2);
        arcBgFill.innerRadius(0);
        arcBg.outerRadius(width / 2 * .85);
        arcBg.innerRadius(width / 2 * .76);
    }


    component.render = function () {
        measure();
        component();
        return component;
    };

    component.value = function (data) {
        if (!data) {
            return component;
        }
        value = [data];
        selection.datum([value]);
        return component;
    };


    component.diameter = function (data) {
        if (!data) {
            return component;
        }
        diameter = data;
        return component;
    };


    component.delay = function (data) {
        if (!data) {
            return component;
        }
        delay = data;
        return component;
    };

    component.duration = function (data) {
        if (!data) {
            return component;
        }
        duration = data;
        return component;
    };
    component.progressStyle = function (data) {
        if (!data) {
            return component;
        }
        progressStyle = data;
        return component;
    };

    return component;

}

