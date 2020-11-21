$(document).ready(function () {
    showMovie();
    $("#you_video").hide();

})


function showMovie() {
    $('#movie-box').empty()

    $.ajax({
        type: "GET",
        url: "/api/list",
        data: {},
        success: function (response) {
            let movies = response['movies_list']


            let name = ''

            for (let i = 0; i < movies.length; i++) {
                let movie = movies[i]
                console.log(movie)
                name = movie['name']
                let img = movie['img_url']
                let summary = movie['summary']
                let url = movie['url']
                let id = movie[i]

                let temp_Html = `

<div class="card">
            <div class="row no-gutters">
                <div class="col-auto">
                    <img src="${img}" class="img-fluid" alt="">
                </div>
                <div class="col">
                    <div class="card-block px-2">
                        <h4 class="card-title">${name}</h4>
                        <p class="card-text">${summary}</p>
                        <a  target="_self" href="${url}" style="color: #BCA9F5">네이버 영화   </a>
                        <button onclick="turn_on_mov(this.id)"  class="btn_clr btn" id="${name}" name="${name}">자세히 보기</button>
                    </div>
                </div>
            </div>
            <div class="test_you"></div>

        </div>
        `


                // 7. #star-box에 temp_html을 붙입니다.
                $('#movie-box').append(temp_Html)

            }


        }
    })
}

function videoSearch(key, search, max) {
    let video = ''


    $.get("https://www.googleapis.com/youtube/v3/search?key=" + key
        + "&type=video&part=snippet&maxResults=" + max + "&q=" + search, function (data) {
        console.log(data)

        data.items.forEach(item => {
            video =
                `

<div class="you" style=" float: left; width: 32%; padding:10px">
                <iframe width="420" height="315" src="https://www.youtube.com/embed/${item.id.videoId}" > </iframe>
               </div>

                `

            $(".you_video").append(video)
        });
    })


}

function turn_on_mov(id) {
    let check = document.getElementsByClassName('test_you');
    let API_KEY = "AIzaSyByYZ3-s2bx8hDCMv3ByUOYbxvWyACl4gc"
    let html = `
<hr width="50%" color="white" size="3"><h5 style="background: white;  color: #BCA9F5">${id} -REVIEW YOUTUBE</h5><hr width="50%" color="white" size="3">

`

    let end = `
`
    $(".you_video").empty()
    $(".you_video").append(html)
    let search = id.concat(" 영화 리뷰")
    videoSearch(API_KEY, search, 3)

    $(".you_video").show();
    window.scrollTo(0, 0);

}

var slideIndex = 0;

