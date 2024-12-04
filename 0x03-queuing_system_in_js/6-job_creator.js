import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Job data
const jobData = {
  phoneNumber: '08107172525',
  message: 'This is the code to verify your account',
};

// Create a job in the push notification code queue
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error('Failed to crreate job:', err);
  }
});
