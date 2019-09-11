import React from 'react';
import { List, Avatar, Icon } from 'antd';




const IconText = ({ type, text }) => (
  <span>
    <Icon type={type} style={{ marginRight: 8 }} />
    {text}
  </span>
);


const Articles = (props) => {
    return (
        <List
            itemLayout="vertical"
            size="large"
            pagination={{
            onChange: page => {
                console.log(page);
            },
            pageSize: 3,
            }}
            dataSource={props.data}
            footer={
            <div>
                <b>ant design</b> footer part
            </div>
            }
            renderItem={item => (
            <List.Item
                key={item.title}
                actions={[
                <IconText type="star-o" text="156" key="list-vertical-star-o" />,
                <IconText type="like-o" text="156" key="list-vertical-like-o" />,
                <IconText type="message" text="2" key="list-vertical-message" />,
                ]}
                extra={
                <img
                    width={272}
                    alt="logo"
                    src={item.picture}
                />
                }
            >
                <List.Item.Meta
                avatar={<Avatar src={item.author.picture} />}
                title={<a href={item.href}>{item.title}</a>}
                description={item.bodytext}
                />
                {item.content}
            </List.Item>
            )}
        />
    )
}

export default Articles;