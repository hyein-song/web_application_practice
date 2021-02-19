
function my_func(){
    alert('검색 버튼이 클릭 되었어요')
    //사용자가 입력한 날짜를 가져와서 해당 날짜에 대한 박스오피스 순위를 알려주는 서버 쪽 웹 프로그램 호출
    // 그 결과를 화면에 출력
    let user_date = $('#userInputDate').val()
    let user_key = '681643bcd05e4b13d7491678e0d35e6e'
    let open_api = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
    //let my_url = open_api+ '?key=' +user_key + '&targetDt='+user_date

    //location.href = my_url // 이렇게 처리하면 화면 refresh가 나타나서 작업할 수 없다.
    //위의 문제를 해결하기 위해 Javascript 가 가지고 있는 특별한 통신방식을 이용.
    // AJAX (ex. 댓글)
    // 순수 Javascript AJAX code가 구현하기 너무 어렵고 힘들기 때문에
    // jQuery를 이용해서 구현
    // {} : 자바스크립트의 객체
    $.ajax({
        url : open_api, //호출할 서버쪽 프로그램의 URL
        type : 'GET',
        dataType : "json",
        data : {
            key : user_key,
            targetDt : user_date
        },
        success : function(result){
            //서버로부터 결과 json을 받아옴(success의 인자로 받아옴)
            //json은 단순 문자열이다 => 사용하기 쉽지 않음 (단순 문자열이기 때문)
            // json > javascript 객체로 자동으로 변환(jQuery가 자동으로 바꿔줌)
            $('#my_tbody').empty()

            let movie_list = result['boxOfficeResult']['dailyBoxOfficeList']
            for(let i=0 ; i < movie_list.length ; i++){
                let m_name = movie_list[i].movieNm
                let m_rank = movie_list[i].rank
                let m_sales = movie_list[i].salesAcc
                //let m_openDt = movie_list[i].openDt
                //let m_audi = movie_list[i].audiAcc
                //data를 가져옴 > HTML element생성

                let tr = $('<tr></tr>')
                let rank_td = $('<td></td>').text(m_rank)
                let title_td = $('<td></td>').text(m_name)
                //let audi_td = $('<td></td>').text(m_audi)
                let img_td = $('<td></td>')
                let sales_td = $('<td></td>').text(m_sales)
                let poster_td = $('<td></td>')
                let poster_btn = $('<input />').attr('type', 'button').attr('value','포스터보기')
                // let delete_td = $('<td></td>')
                // let delete_btn = $('<input />').attr('type', 'button').attr('value','삭제')
                //let open_td = $('<td></td>').text(m_openDt)

                // delete_td.on('click', function(){
                //     $(this).parent().parent().remove()
                // })
                poster_td.append(poster_btn)

                poster_btn.on('click', function(){
                    // keyword = '건축학개론'

                    $.ajax({
                        url :'https://dapi.kakao.com/v2/search/image',
                        type : 'GET',
                        dataType : 'json',
                        data : {
                            query : m_name + ' 포스터'
                        },
                        headers : {
                            Authorization: 'KakaoAK 186934589f97ebd7d4df85f2b65d4f7d'

                        },
                        success : function (result){
                            alert(m_name)

                            let img_url = result['documents'][0]['thumbnail_url']
                            let img_btn = $('<img/>').attr('src',img_url)
                            img_td.append(img_btn)
                            //$(this).parent().children('img_td').append(img_btn)
                            //<img src="image/cat.jpg">

                        },
                        error : function (){
                            alert('실패')

                        }
                    })
                })



                //delete_td.append(delete_btn)
                tr.append(rank_td) // 맨 마지막 자식
                tr.append(title_td)
                tr.append(img_td)
                //tr.append(audi_td)
                tr.append(sales_td)
                tr.append(poster_td)
                //tr.append(delete_td)
                //tr.append(open_td)

                $('#my_tbody').append(tr)

            }
        },
        error : function (){
            alert('뭔가 이상해요!')

        }

    })

}