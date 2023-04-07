from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
blog = {
    'name': 'My Awesome Blog',
    'posts': {
        # 1 : {
        #	'post_id' : 1,
        #	'title' : 'First Post',
        #	'content' : 'Hey there !'
        # },
        # 2 : {
        #	'post_id' : 2,
        #	'title' : 'Second Post',
        #	'content' : 'How you doing !'
        # }
    }

}


@app.route('/')
def Hello():
    return render_template('home.jinja2', blog=blog)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = blog['posts'].get(post_id)
    # return post['title']

    if post is None:
        return render_template('404.jinja2', message=f'A post with post id {post_id} was not found !')

    return render_template('post.jinja2', the_post=post)


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(blog['posts'])
        blog['posts'][post_id] = {'post_id': post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id=post_id))

    return render_template('create.html')


app.run()
