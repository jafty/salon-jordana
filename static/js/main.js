const homeView = document.getElementById('home-view');
const articleView = document.getElementById('article-view');

function showArticle() {
    if (!homeView || !articleView) return;
    homeView.style.display = 'none';
    articleView.style.display = 'block';
    window.scrollTo(0, 0);
}

function showHome() {
    if (!homeView || !articleView) return;
    articleView.style.display = 'none';
    homeView.style.display = 'block';
    window.scrollTo(0, 0);
}
