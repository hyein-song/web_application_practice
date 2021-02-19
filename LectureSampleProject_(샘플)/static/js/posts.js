
function new_post() {
    $(location).attr('href','/bbs/create');
}

function to_list() {
    $(location).attr('href','/bbs/list');
}

function delete_post(post_id) {
    let result = confirm('정말 삭제할까요?')
    if(result) {
        $(location).attr('href','/bbs/delete/' + post_id);
    }
}

function update_post(post_id) {
        $(location).attr('href','/bbs/update/' + post_id);
}

