from flask import Flask, jsonify, request
from model.blog_post import BlogPost 
from model.user import User

def custom_json_serializer(obj):
    if isinstance(obj, User):
        return {'username': obj.username}
    elif isinstance(obj, BlogPost):
        return {'body': obj.body, 'author': obj.author}
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

blogposts = []

app = Flask(__name__)
app.json.default = custom_json_serializer

@app.route('/ping', methods=['GET'])
def index():
    return jsonify({'response': 'pong'})

@app.route('/blogpost', methods=['POST'])
def create_blogpost():
    blogpost_json = request.get_json()
    author = User(blogpost_json['author'])
    blogpost = BlogPost(blogpost_json['body'], author)
    blogposts.append(blogpost)
    return jsonify({'status': 'success'})

@app.route('/blogpost', methods=['GET'])
def read_blogposts():
    return jsonify({'blogposts': blogposts})

@app.route('/blogpost/<int:post_id>', methods=['PUT'])
def update_blogpost(post_id):
    if post_id < 0 or post_id >= len(blogposts):
        return jsonify({'error': 'Blog post not found'}), 404
    
    blogpost_json = request.get_json()
    author = User(blogpost_json['author'])
    blogposts[post_id] = BlogPost(blogpost_json['body'], author)
    return jsonify({'status': 'success', 'message': 'Blog post updated'})

@app.route('/blogpost/<int:post_id>', methods=['DELETE'])
def delete_blogpost(post_id):
    if post_id < 0 or post_id >= len(blogposts):
        return jsonify({'error': 'Blog post not found'}), 404
    
    deleted_post = blogposts.pop(post_id)
    return jsonify({'status': 'success', 'message': 'Blog post deleted', 'deleted_post': deleted_post})




if __name__ == '__main__':
    app.run(debug=True)





