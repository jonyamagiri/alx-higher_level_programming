#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) console.log(error);

  const taskCount = {};
  const tasks = JSON.parse(body);

  tasks.forEach(task => {
    if (!task.completed) {
      return;
    }
    const userId = task.userId;
    taskCount[userId] = taskCount[userId] ? taskCount[userId] + 1 : 1;
  });
  console.log(taskCount);
});
