$(document).ready(function() {
 let API_KEY="AIzaSyByYZ3-s2bx8hDCMv3ByUOYbxvWyACl4gc"
        $("form").submit(function (event){
            event.preventDefault()
        let search = "ajax"
        videoSearch(API_KEY, search,3)
        })



    function videoSearch(key,search,max){
        $("#videos").empty()


        $.get("https://www.googleapis.com/youtube/v3/search?key="+key
            + "&type=video&part=snippet&maxResults="+max+"&q="+search,function (data){
            console.log(data)

            data.items.forEach(item => {
                video =
                `
        
                <iframe width="420" height="315" src="https://www.youtube.com/embed/${item.id.videoId}" > </iframe>
                
                `

                $("#videos").append(video)
            });
        })


    }

})