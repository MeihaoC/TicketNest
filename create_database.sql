-- After connecting to the Aiven database,
-- 1. USE defaultdb;
-- 2. SOURCE the following SQL script to create tables.
CREATE TABLE `User` (
	`user_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`user_name` VARCHAR(255) NOT NULL,
	`email` VARCHAR(255) NOT NULL,
	`password` VARCHAR(255) NOT NULL,
	`phone` VARCHAR(255) NOT NULL,
	`gender` ENUM ('Female', 'Male', 'Other') NOT NULL,
	`birthday` DATE NOT NULL,
	`account_status` ENUM ('Activated', 'Deactivated') NOT NULL,
	PRIMARY KEY(`user_id`)
);


CREATE TABLE `Event` (
	`event_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`event_category` ENUM ('Concert', 'Festival', 'Sports event', 'Theatre') NOT NULL,
	`location` VARCHAR(255) NOT NULL,
	`date` DATE NOT NULL,
	`description` TEXT(65535) NOT NULL,
	`event_name` VARCHAR(255) NOT NULL,
	`artist_team` VARCHAR(255) NOT NULL,
	`event_status` ENUM ('Active', 'Past', 'Canceled') NOT NULL,
	PRIMARY KEY(`event_id`)
);


CREATE TABLE `Ticket` (
	`ticket_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`event_id` INTEGER NOT NULL,
	`ticket_type` ENUM ('General Admission', 'VIP') NOT NULL,
	`price` DECIMAL NOT NULL,
	`quantity_available` INTEGER NOT NULL,
	PRIMARY KEY(`ticket_id`)
);


CREATE TABLE `Order` (
	`order_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`user_id` INTEGER NOT NULL,
	`purchase_date` DATE NOT NULL,
	`order_status` ENUM ('Completed', 'Failed') NOT NULL,
	`payment_method` ENUM ('Credit/debit', 'Paypal') NOT NULL,
	PRIMARY KEY(`order_id`)
);


CREATE TABLE `Refund` (
	`refund_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`order_ticket_id` INTEGER NOT NULL,
	`quantity_refund` INTEGER NOT NULL,
	`refund_date` DATE NOT NULL,
	`refund_status` ENUM ('Approved', 'Declined') NOT NULL,
	PRIMARY KEY(`refund_id`)
);


CREATE TABLE `Review` (
	`review_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`event_id` INTEGER NOT NULL,
	`user_id` INTEGER NOT NULL,
	`rating` DECIMAL(2,1) NOT NULL CHECK (rating >= 1 AND rating <= 10),
	`comment` TEXT(65535),
	`review_status` ENUM ('Approved', 'Rejected', 'Pending') NOT NULL,
	PRIMARY KEY(`review_id`)
);


CREATE TABLE `Notification` (
	`notification_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`event_id` INTEGER NOT NULL,
	`preference_id` INTEGER NOT NULL,
	`content` TEXT(65535) NOT NULL,
	`notify_date` DATE NOT NULL,
	PRIMARY KEY(`notification_id`)
);


CREATE TABLE `UserNotification` (
	`user_notification_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`user_id` INTEGER NOT NULL,
	`notification_id` INTEGER NOT NULL,
	`is_opt_in` BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY(`user_notification_id`)
);


CREATE TABLE `OrderTicket` (
	`order_ticket_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`order_id` INTEGER NOT NULL,
	`ticket_id` INTEGER NOT NULL,
	`quantity_purchase` INTEGER NOT NULL,
	PRIMARY KEY(`order_ticket_id`)
);


CREATE TABLE `UserLoginHistory` (
	`login_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`user_id` INTEGER NOT NULL,
	`login_time` TIMESTAMP NOT NULL,
	PRIMARY KEY(`login_id`)
);


CREATE TABLE `Preference` (
	`preference_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`preference_type` ENUM ('Upcoming events', 'Ticket availability', 'Special promotions', 'Concert', 'Sports', 'Theatre') NOT NULL,
	PRIMARY KEY(`preference_id`)
);


CREATE TABLE `UserPreference` (
	`user_id` INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
	`preference_id` INTEGER NOT NULL,
	PRIMARY KEY(`user_id`, `preference_id`)
);


ALTER TABLE `Review`
ADD FOREIGN KEY(`event_id`) REFERENCES `Event`(`event_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `Review`
ADD FOREIGN KEY(`user_id`) REFERENCES `User`(`user_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `UserNotification`
ADD FOREIGN KEY(`notification_id`) REFERENCES `Notification`(`notification_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;


ALTER TABLE `UserNotification`
ADD FOREIGN KEY(`user_id`) REFERENCES `User`(`user_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `Order`
ADD FOREIGN KEY(`user_id`) REFERENCES `User`(`user_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `Ticket`
ADD FOREIGN KEY(`event_id`) REFERENCES `Event`(`event_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `OrderTicket`
ADD FOREIGN KEY(`ticket_id`) REFERENCES `Ticket`(`ticket_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `OrderTicket`
ADD FOREIGN KEY(`order_id`) REFERENCES `Order`(`order_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `Refund`
ADD FOREIGN KEY(`order_ticket_id`) REFERENCES `OrderTicket`(`order_ticket_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `UserLoginHistory`
ADD FOREIGN KEY(`user_id`) REFERENCES `User`(`user_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `UserPreference`
ADD FOREIGN KEY(`user_id`) REFERENCES `User`(`user_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `UserPreference`
ADD FOREIGN KEY(`preference_id`) REFERENCES `Preference`(`preference_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `Notification`
ADD FOREIGN KEY(`event_id`) REFERENCES `Event`(`event_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;

ALTER TABLE `Notification`
ADD FOREIGN KEY(`preference_id`) REFERENCES `Preference`(`preference_id`)
ON UPDATE NO ACTION ON DELETE NO ACTION;