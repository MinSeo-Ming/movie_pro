$(document).ready(function() {

        get
        let movie = "기생충"
        videoSearch(API_KEY, 3)


    function videoSearch(key,search,max){
        $("#you_video").empty()
        let search=''

        $.get("https://www.googleapis.com/youtube/v3/search?key="+key
            + "&type=video&part=snippet&maxResults="+max+"&q="+search,function (data){
            console.log(data)

            data.items.forEach(item => {
                video =
                `
                <div class ="you">
                <iframe width="420" height="315" src="https://www.youtube.com/embed/${item.id.videoId}" > </iframe>
                </div>
                `

                $("#you_video").append(video)
            });
        })


    }

})