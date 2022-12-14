window.onload = async function() {
    // elem.insertAdjacentHTML('beforeend', str)
    const xhttp = new XMLHttpRequest();
    xhttp.onload = async function() {
        data = JSON.parse(this.response)['data'] 
        if (data.length>0){
            data.forEach(async (val)=>{
                str = '<div class="w3-third w3-container w3-margin-bottom">\
                        <img src="'+val['media_url'].split(',')[0]+ '" alt="Norway" style="width:100%" class="w3-hover-opacity">\
                        <div class="w3-container w3-white">\
                        <p><b>'+val['text']+'</b></p>\
                        <p>Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida diam non fringilla.</p>\
                        </div>\
                        </div>'
                document.getElementById('post-div').insertAdjacentHTML('beforeend', str);
            }
            )
        }
        else{
            document.getElementById('post-div').insertAdjacentHTML('beforeend', '<p>No feeds to show</p>');
        } 
        }
    xhttp.open("GET", "/post/feed", true);
    xhttp.send();
}
