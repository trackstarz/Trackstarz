import React from 'react';
import { List, Avatar } from 'antd';

const IconText = ({ type, text }) => (
  <span>
    {text}
  </span>
);

const data = [
  {
    author: 'John Doe',
    bodytext: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    createdAt: '2022-02-14T17:30:35.572Z',
    id: 1,
    likeCount: 10,
    username: 'johndoe'
  },
  {
    author: 'Jane Smith',
    bodytext: 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.',
    createdAt: '2022-02-15T14:20:05.212Z',
    id: 2,
    likeCount: 20,
    username: 'janesmith'
  },
  {
    author: 'Bob Johnson',
    bodytext: 'Itaque earum rerum hic tenetur a sapiente delectus.',
    createdAt: '2022-02-16T08:45:10.990Z',
    id: 3,
    likeCount: 5,
    username: 'bobjohnson'
  },
];

const Bursts = (props) => {
  return (
    <List
      itemLayout="vertical"
      dataSource={data}
      renderItem={item => (
        <List.Item
          key={item.id}
          actions={[
            <IconText type="like-o" text={item.likeCount} key="list-like-o" />,
          ]}
        >
          <List.Item.Meta
            avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}
            title={<a href={`/${item.username}`}>{item.author}</a>}
            description={item.createdAt}
          />
          {item.bodytext}
        </List.Item>
      )}
    />
  );
}

export default Bursts;
