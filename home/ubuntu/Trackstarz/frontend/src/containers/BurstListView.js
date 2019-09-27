import React from 'react';
import axios from 'axios';
import {connect} from 'react-redux';
import Bursts from '../components/Burst';
import BurstForm from '../components/BurstForm';
import '../style.css';
import CommentForm from '../components/CommentForm';




class BurstList extends React.Component {
    
    state = {
        bursts: [],
        userprofiles: [],
        users: [],
        comments: [],
        replies: []
    }

    fetchBursts = () => {
        axios.get('http://34.222.26.155:8080/api/bursts/')
            .then(res => {
                this.setState({
                    bursts: res.data
                });
            });
    }

    fetchComments = () => {
        axios.get('http://34.222.26.155:8080/api/comments/')
            .then(res => {
                this.setState({
                    comments: res.data
                });
            });
    }


    fetchReplies = () => {
        axios.get('http://34.222.26.155:8080/api/replies/')
            .then(res => {
                this.setState({
                    replies: res.data
                });
            });
    }

    fetchUserProfiles = () => {
        axios.get('http://34.222.26.155:8080/api/userprofiles/')
            .then(res => {
                this.setState({
                    userprofiles: res.data
                });
            });
    }

    fetchUsers = () => {
        axios.get('http://34.222.26.155:8080/api/users/')
            .then(res => {
                this.setState({
                    users: res.data
                });
            });
    }

   

    componentWillReceiveProps(newProps) {
        console.log(newProps);
        if(newProps.token) {
            axios.defaults.headers = {
                "Content-Type": "application/json",
                Authorization: newProps.token
            }
            this.fetchBursts();
            this.fetchUserProfiles();
            this.fetchUsers();
            this.fetchComments();
            this.fetchReplies();
            
        }
    }
    
    render() {
        return (
            <div>
                <div style={{ marginBottom: 10, borderRadius: 5, padding: 10, background: '#fff'}}>
                    <BurstForm 
                        requestType="post"
                        burstID={null}
                        btnText="post"/>
                </div>
                    <Bursts data={this.state.bursts}/>
                    <div >
                            {this.state.bursts.map(burst => (
                                <div className="burst">
                                
                                { burst.author != null &&
                                <div>
                                <img src={ burst.author.picture } style={{ objectFit: "cover", objectPosition: "50% 0", width: 40, height: 40, borderRadius: "50%"}} /> 
                                
                                <b>  {burst.author.displayname}</b> <small><b>@{burst.author.user.username}</b></small> <small> {burst.timestamp}</small>
                                </div>
                                }
                                { burst.title != null &&
                                <h2>{burst.title}</h2>
                                }
                                <p>{burst.bodytext}</p>
                                { burst.picture != null &&
                                <img src={burst.picture} width='100%' />
                                }
                                
                                <hr/>
                                <br/>
                                <hr/>
                                <br/>
                                <hr/>
                                <CommentForm
                                    requestType="post"
                                    commentID={null}
                                    burstID={burst.id}
                                    btnText="post" />
                                {this.state.comments.filter(comment => burst.id === comment.burst).map(comment => (
                                    <div className="comments">
                                        <h4><img src={ comment.author.picture } id="comment_image" /> 
                                
                                        <b>  {comment.author.displayname}</b> <small><b>@{comment.author.user.username}</b></small> <small> {comment.timestamp}</small></h4>
                                        <div>{comment.content}</div>
                                        {this.state.replies.filter(reply => comment.id === reply.comment.id).map(reply => (
                                            <div className="reply">
                                                <h4><small>
                                                <img src={ reply.author.picture } id="comment_image" /> 
                                
                                                <b>  {reply.author.displayname}</b> <small><b>@{reply.author.user.username}</b></small> <small> {reply.timestamp}</small></small></h4>
                                                <div>{reply.content}</div>
                                            </div>
                                        ))}
                                    </div>
                                )).sort().reverse()}
                               </div>
                        
                             )).sort().reverse()}
                             
                  
                    </div>
            </div>
        )
    }
}

const mapStateToProps = state => {
    return {
      token: state.token
    }
  }


export default connect(mapStateToProps)(BurstList);