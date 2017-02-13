function criarDatatable( idElemento, dados, labels, order, callback ){
    var i,j;
    var divPai = $('#'+idElemento);

    //limpa o conteúdo
    divPai.empty();

    var divResponsive = $('<div/>')
        .attr('class','table-responsive');

    divPai.append(divResponsive);

    var tabela = $('<table/>')
        .attr('id','tabela_'+idElemento)
        .attr('class','table table-striped table-bordered')
        .attr('cellspacing','0')
        .attr('width','100%')
        ;

    divResponsive.append(tabela);

    var thead = $('<thead/>')
        .attr('class','thead-inverse')
        .appendTo(tabela);

    var tr = $('<tr/>')
        .appendTo(thead);

    for(i=0;i<labels.length;i++){
        var th = $('<th/>')
            .html(labels[i])
            .appendTo(tr);
    }

    var tbody = $('<tbody/>')
        .appendTo(tabela);

    for(i=0;i<dados.length;i++){
        linha = dados[i];

        tr = $('<tr/>')
            .attr('data-row-index',i)
            .appendTo(tbody);

        for(j=0;j<linha.length;j++){
            var th = $('<td/>')
                .html(linha[j])
                .appendTo(tr);
        }

    }


//    tabela.DataTable({
//        "language": traducoesDatatable,
//        "order": [order],
//        "paginate": true
//    }).on('dblclick', 'tr', function(event) {
//        if( callback ){
//            callback(event);
//        }
//    });

}

function formatMoney(value, c, d, t){
	var n = value, 
	    c = isNaN(c = Math.abs(c)) ? 2 : c, 
	    d = d == undefined ? "." : d, 
	    t = t == undefined ? "," : t, 
	    s = n < 0 ? "-" : "", 
	    i = String(parseInt(n = Math.abs(Number(n) || 0).toFixed(c))), 
	    j = (j = i.length) > 3 ? j % 3 : 0;
	   return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
};

function rolagem_foco(idElemento, deslocamento){

    if( !deslocamento )
        deslocamento = 70;
    $('html,body').animate({scrollTop: $("#"+idElemento).offset().top - deslocamento},'slow');
}

function menuPaginacaoPadrao(){
    return [[5, 10, 25, 50, 100, -1], [5, 10, 25, 50, 100, "Todos"]];
}