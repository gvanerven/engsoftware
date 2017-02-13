

function grafico_barra(config){

    //id da div pai onde o gráfico deve ser inserido
    var id_elemento = config['id_elemento'];
    var data = config ['dados'];
    var rotulos = config ['rotulos'];
    var f_callback_onclick = config['onclick'];

    var wrapperElemento = $('#'+id_elemento);

    var widthElemento = wrapperElemento.width();
    var heightElemento = wrapperElemento.height();

    wrapperElemento.empty();

    var svg = d3.select('#'+id_elemento)
            .append("svg")
            .attr("width", widthElemento)
            .attr("height", heightElemento)
//            .style('shape-rendering','geometricPrecision')
            ;

    var margin = {top: 20, right: 20, bottom: 30, left: 40},

    width = widthElemento - margin.left - margin.right;
    height = heightElemento - margin.top - margin.bottom;


    var x = d3.scaleBand().rangeRound([0, width]).padding(0.1);
    var y = d3.scaleLinear().rangeRound([height, 0]);


    var g = svg.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");


    x.domain(data.map(function(d) { return parseInt(d[1]+'0'+d[0]); }));
    y.domain([0, d3.max(data, function(d) { return d[2]; })]);

    formatYLabel = d3.format("d");

    g.append("g")
        .attr("class", "axis axis--x")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));


    g.append("g")
        .attr("class", "axis axis--y")
        .call(d3.axisLeft(y)
            .ticks(10, "")
            .tickFormat(function(d){return formatYLabel(d) })
            )

    .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")
        .text(rotulos[2]);


    g.selectAll(".bar")
    .data(data)
    .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function(d,i) { return x(d[1] + '0' + d[0]); })
        .attr("y", function(d,i) { return y(d[2]); })
        .attr("width", x.bandwidth())
        .attr("height", function(d) { return height - y(d[2]); })
        .style("cursor","hand")
        .on('click', function(d,i){ f_callback_onclick(d,i); })
        ;

}