import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';


describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue();

  // Before each test, enable test mode
  beforeEach(() => {
    kue.Job.queue.testMode.enter();
  });

  // After each test, clear and exit test mode
  afterEach(() => {
    kue.Job.queue.testMode.clear();
    kue.Job.queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const jobs = [
      {
	phoneNumber: '08107172525',
	message: 'This is the code 1234 to verify your account' },
      
      {
	phoneNumber: '08107172526',
	message: 'This is the code 4562 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  it('should log correct messages when jobs are created', () => {
    const jobs = [
      {
        phoneNumber: '08107172525',
        message: 'This is the code 1234 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];
    expect(job).to.exist;
    expect(job.type).to.equal('push_notification_code_3');
    expect(jobs.data.phoneNumber).to.equal('08107172525');
  });
});
