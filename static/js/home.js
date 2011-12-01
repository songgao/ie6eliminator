function generate(){
    if($("#original_url").val().length==0)
        return;

    var gen_url = $(location).attr('protocol')+"//"+$(location).attr('host')+"/check?url="+$.URLEncode($("#original_url").val());
    var buttonGenerateHtml = $("#buttonGenerate").html();
    $("#buttonGenerate").html(buttonGenerateHtml.replace("Generate and Shorten", "Shortening..."));
    $.post('/shorten', {"url":gen_url}, function(data) {
        short_url=data['id'];
        $("#generated").html(
            '<div id="instruction">Send the following URL to your friend, or post it online. IE6 Eliminator will check the visitor\'s browser and help eliminating IE6.</div><div id="generated_url">' + '<a href="'+short_url+'" title="'+gen_url+'" >'+short_url+'</a>' + '</div>'
            +'<form action="/preview" target="_blank" method="POST"><input type="hidden" name="url" value="'+$("#original_url").val()+'">'
            +'<button type="submit" id="buttonpreview" class="button">ie6 preview</button></form>'
        );
        $("#buttonpreview").button();
            $("#buttonGenerate").html(buttonGenerateHtml);
    }, "json");
}

$(document).ready(function() {
        $("#buttonGenerate").click(generate);
        $("#buttonGenerate").button();
        $('#original_url').keyup(function(e) {
            if(e.keyCode == 13) {
                event.preventDefault();
                $("#buttonGenerate").click();
            }
        });
});

