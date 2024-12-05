const kue = require('kue');

// Create a kue queue
const queue = kue.createQueue();

// Create array
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function
const sendNotification = (phoneNumber, message, job, done) => {
    
    // Track job progress
    job.progress(0, 100);

    // Check if the phone number is blacklisted
    if (blacklistedNumbers.includes(phoneNumber)) {
	return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    done();
};

// Process jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});


// Create a job for the queue
const createJobs = () => {
    const messages = [
	{ phoneNumber: '4153518743', message: 'This is the code 4321 to verify your account' },
        { phoneNumber: '4153538781', message: 'This is the code 4562 to verify your account' },
        { phoneNumber: '4153118782', message: 'This is the code 4321 to verify your account' },
        { phoneNumber: '4153718781', message: 'This is the code 4562 to verify your account' },
        { phoneNumber: '4159518782', message: 'This is the code 4321 to verify your account' },
        { phoneNumber: '4158718781', message: 'This is the code 4562 to verify your account' },
        { phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' },
        { phoneNumber: '4154318781', message: 'This is the code 4562 to verify your account' },
        { phoneNumber: '4151218782', message: 'This is the code 4321 to verify your account' }
    ];

    messages.forEach(({ phoneNumber, message }) => {
	const job = queue.create('push_notification_code_2', { phoneNumber, message }).save();
    

	job.on('complete', () => console.log(`Notification job #${job.id} completed`))
	   .on('failed', (err) => console.log(`Notification job #${job.id} failed: ${err.message}`))
	   .on('progress', (progress) => console.log(`Notification job #${job.id} ${progress}% complete`));

	job.progress((job, done) => {
	    sendNotification(job.data.phoneNumber, job.data.message, job, done);
        });
    });
};

// Start the job creation
if (require.main === module) {
    createJobs();
}

