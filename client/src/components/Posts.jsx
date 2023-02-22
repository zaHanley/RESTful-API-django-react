import React, { useState, useEffect } from "react";
import axios from "axios";

function Posts() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const getPosts = async () => {
      let response = await axios.get("http://127.0.0.1:8000/api/");
      let data = await response.data;
      setPosts(data);
    };

    getPosts();
  }, []);
  return (
    <>
      {posts.map((post) => (
        <div className="card border-light mb-3">
          <div className="card-header">{post.title}</div>
          <div className="card-body">
            <p className="card-text">{post.content}</p>
          </div>
        </div>
      ))}
    </>
  );
}

export default Posts;
