var meeting_num = 2;

function getQueryParams(qs) {
    qs = qs.split('+').join(' ');

    var params = {},
        tokens,
        re = /[?&]?([^=]+)=([^&]*)/g;

    while (tokens = re.exec(qs)) {
        params[decodeURIComponent(tokens[1])] = decodeURIComponent(tokens[2]);
    }

    return params;
}

window.location.pathname_with_query_string = function(){
    return this.href.substring(this.origin.length);
 };

window.loginRequired = function (cb) {
    api.get('/api/a/login', {}, cb, function () {
        window.location.href = '/a/login?' + $.param({
            next: window.location.pathname_with_query_string()
        });
    });
};

window.logout = function () {
    api.get('/api/u/logout', {}, function () {
        window.location.href = '/user/login';
    }, dftFail);
};

window.updateObj = function (obj, newObj) {
    for (var key in newObj) {
        obj[key] = newObj[key];
    }
};
