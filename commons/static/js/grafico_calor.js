

function grafico_calor(config){

    //id da div pai onde o gráfico deve ser inserido
    var id_elemento = config['id_elemento'];
    var data = config ['dados'];
    var rotulos = config ['rotulos'];
    var f_callback_onclick = config['onclick'];

    var wrapperElemento = $('#'+id_elemento);

    var widthElemento = wrapperElemento.width();
    var heightElemento = widthElemento/2;//wrapperElemento.height();

    wrapperElemento.empty();

    var div = d3.select("body").append("div")
        .attr("id", "grafico_calor_tooltip")
        .attr("class", "tooltip")
        .style("opacity", 0);

    var svg = d3.select('#'+id_elemento)
            .append("svg")
            .attr("width", widthElemento)
            .attr("height", heightElemento)
//            .style('shape-rendering','geometricPrecision')
            ;

    var margin = {top: 30, right: 20, bottom: 40, left: 40};

    var width = widthElemento - margin.left - margin.right;
    var height = heightElemento - margin.top - margin.bottom;

    var gridSizeW = width / (d3.max(data, function(d) { return d[1]; })+1);
    var gridSizeH = height / (d3.max(data, function(d) { return d[2]; })+1);

    var colorScale = d3.scaleLinear()
        .domain([0,d3.max(data, function(d) { return d[0]; })])
        .range(['white', 'green']);

    x = d3.scaleLinear().range([0, width]);
    y = d3.scaleLinear().range([height, 0]);

    x.domain([0, d3.max(data, function(d) { return d[1]; })+1]).nice();
    y.domain([0, d3.max(data, function(d) { return d[2]; })+1]).nice();

    formatYLabel = d3.format("d");

    var g = svg.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

/*
    g.append("rect")
        .attr("x", 100)
        .attr("y", 200)
        .attr("width", 200)
        .attr("height", 300)
        .style("fill", "blue")
        .style("stroke", "black")
*/


    g.append('g').selectAll(".bar")
    .data(data)
    .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function(d,i) { return x(d[1]); })
        .attr("y", function(d,i) { return y(d[2]+1); })
        .attr("width", gridSizeW)
        .attr("height", gridSizeH)
        .style("fill", function(d,i) { return colorScale(d[0]); })
//        .style("fill-opacity", 0.7)
//        .style("stroke", 3)
//        .style("stroke-color", "gray")
//        .style("cursor","hand")
        .on('click', function(d,i){ f_callback_onclick(d,i); })
        .on("mouseover", function(d) {
            var divdd = d3.select('#grafico_calor_tooltip');
            divdd.transition()
                .duration(200)
                .style("opacity", .9);
            divdd.html('Similaridade: ' + d[0] + "<br/>Idx1: " + d[1] + "<br/>Idx2: " + d[2])
                .style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
            })
        .on("mouseout", function(d) {
            var divdd = d3.select('#grafico_calor_tooltip');
            divdd.transition()
                .duration(100)
                .style("opacity", 0);
        })
        ;


    g.append("g")
        .attr("class", "axis axis_x")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));


    g.append("g")
        .attr("class", "axis axis_y")
        .call(d3.axisLeft(y)
//            .ticks(10, "Teste")
//            .tickFormat(function(d){return formatYLabel(d) })
            )

    g.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", -26)
        .attr("text-anchor", "end")
        .text(rotulos['y']);

    g.append("text")
        .attr("x", width)
        .attr("y", height + 26)
        .attr("text-anchor", "end")
        .text(rotulos['x']);

}