-- MySQL Compatible Insert Statements for Sistem Pencatatan Penginapan Kos
-- Generated: 2025-05-13 08:31:21

SET FOREIGN_KEY_CHECKS=0;

-- TRUNCATE statements to clear existing data
TRUNCATE TABLE occupancy_records;
TRUNCATE TABLE financial_records;
TRUNCATE TABLE rooms;
TRUNCATE TABLE national_holidays;
TRUNCATE TABLE properties;
TRUNCATE TABLE users;

-- Data for table users
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (1, 'admin', 'scrypt:32768:8:1$9LhLG4oAm05tqRI3$9918004a92b5dcb761a2b0e3b08dc3ede7cae42155de72bd0bc1b847d62224ce5fbe280bdbb0472abdbb7929fa097276e10e19d0bd4cf30fc0b5e1c1f90ec7fe', 'admin', NULL, '2025-05-12 09:26:15');
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (2, 'karawang1', 'scrypt:32768:8:1$BB9ItHrlSqLIQi0d$63275fcd5dfc62a8aad14511c85b5b4e1c5bc2562fa941f393f2349220e43079c0ac1c0d37f3538a3ccc21b07ae578fabd594324a266d2aa989853fe1160fbb2', 'user', NULL, '2025-05-12 09:26:15');
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (3, 'karawang2', 'scrypt:32768:8:1$eA3v99dL8VICMNsr$89279799dce555a6cbad99ab31d83e14b59efeb57c7cbdb82a298b0452fc2c247130fc7d9cadb405d0d1b51d9d6a1f2169849eea9009d92ae96f7025a10d8f2a', 'user', NULL, '2025-05-12 09:26:15');
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (4, 'bandung', 'scrypt:32768:8:1$mDc1lpaaMEuOY1ku$52ab88ade95b00c82e31fe8f0f76ff32d5f748eaa358240fcd305bf7b14dc4d1b856190e56c1439137c8d8616daa9dc18c931943840e8154031d5ed3ecf4d334', 'user', NULL, '2025-05-12 09:26:16');
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (5, 'manager1', 'scrypt:32768:8:1$yOP17unOz3DEmu8T$e9933a3c9614d3c3aca3d60a026618bb84c87f0a335699fb96a8fa2de1b799671d513ab9145f82e1751ac6faa7aa596c31d9d9a2a29e6055c7c9bfde2cfe5727', 'manager', 'KOS ANTAPANI', '2025-05-12 10:24:22');
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (7, 'staff1', 'scrypt:32768:8:1$PY8gMgiAlIdWxx1k$8308711eaf8e3237d5e85d45996c9ad80aae8200413a155fda5c682c42333b570bc6108e7a39f35e388160236d103b987e44b52d288e8a038fc2cb0b2fe9a758', 'staff', 'KOS ANTAPANI', '2025-05-12 10:24:23');
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (8, 'staff2', 'scrypt:32768:8:1$1cxDcmav05CZKiuW$ce73c58ed6bef10f6a82c61c9a5a2aa8dec79098e7aeb3394ab25599dbecc1fb9adca2e8142fce79a6bd85a0c1d697607a50da88e961126c3ef0204ef4522611', 'staff', 'KOS GURO', '2025-05-12 10:24:23');
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (9, 'staff3', 'scrypt:32768:8:1$XEjXeKsZ8v4Ybr8F$5567d4574894682d4af2361c2edf1a644ff0a1fb1dc53aa6ad45f2149b3388494097c59ee4ebcc8bf5cd0c8a7dbf805259360c0dc94087dfffe4d41228ecf135', 'staff', 'KOS PESONA GRIYA', '2025-05-12 10:24:23');
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (10, 'viewer1', 'scrypt:32768:8:1$AutiYta2k593jjU5$7da02cc7b0bce739265bbbc294d1a4ee630a5aaf878176f07990d76df7b32c6a2c424c1b1e976e0e3d47c1a907860fabe69f34afa44cacade32ce6c47da7f22b', 'viewer', '', '2025-05-12 10:24:23');
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (11, 'manager3', 'scrypt:32768:8:1$zxY1Zen5kQ9QJmFR$13a9cfb6c73a8b1b11507c902c017a5109125ba665becd25388ffb68cffd8c60f5be8eebcf4cbe84d2488df33bc08e8035155f3b3a2c6d84207360f2d6148ead', 'manager', 'KOS PESONA GRIYA', '2025-05-12 10:42:27');
INSERT INTO users (id, username, password_hash, role, location, created_at) VALUES (6, 'manager2', 'scrypt:32768:8:1$P1E6iPsLFPzs2kdL$6361e1c594bd20a9dc21c8299dae43be2cedfee2c28973733974e9ed358b5613a85ae7f4056ebbd7c00b58560d7b98bc38ed9c9cb8294db4f1857bd2f76d23d8', 'manager', 'KOS GURO', '2025-05-12 10:24:22');

-- Data for table properties
INSERT INTO properties (id, name, address, total_rooms, created_at) VALUES (1, 'KOS ANTAPANI', 'Antapani, Bandung', 10, '2025-05-12 09:26:16');
INSERT INTO properties (id, name, address, total_rooms, created_at) VALUES (2, 'KOS GURO', 'Karawang', 8, '2025-05-12 09:26:16');
INSERT INTO properties (id, name, address, total_rooms, created_at) VALUES (3, 'KOS PESONA GRIYA', 'Karawang', 12, '2025-05-12 09:26:16');

-- Data for table national_holidays
INSERT INTO national_holidays (id, date, name, created_at) VALUES (1, '2025-01-01', 'Tahun Baru Masehi', '2025-05-12 09:26:16');
INSERT INTO national_holidays (id, date, name, created_at) VALUES (2, '2025-03-31', 'Hari Raya Nyepi', '2025-05-12 09:26:16');
INSERT INTO national_holidays (id, date, name, created_at) VALUES (3, '2025-04-18', 'Wafat Isa Almasih', '2025-05-12 09:26:16');
INSERT INTO national_holidays (id, date, name, created_at) VALUES (4, '2025-05-01', 'Hari Buruh', '2025-05-12 09:26:16');
INSERT INTO national_holidays (id, date, name, created_at) VALUES (5, '2025-05-29', 'Kenaikan Isa Almasih', '2025-05-12 09:26:16');
INSERT INTO national_holidays (id, date, name, created_at) VALUES (6, '2025-06-01', 'Hari Lahir Pancasila', '2025-05-12 09:26:16');
INSERT INTO national_holidays (id, date, name, created_at) VALUES (7, '2025-06-06', 'Hari Raya Idul Adha', '2025-05-12 09:26:16');
INSERT INTO national_holidays (id, date, name, created_at) VALUES (8, '2025-07-17', 'Tahun Baru Islam', '2025-05-12 09:26:16');
INSERT INTO national_holidays (id, date, name, created_at) VALUES (9, '2025-08-17', 'Hari Kemerdekaan RI', '2025-05-12 09:26:16');
INSERT INTO national_holidays (id, date, name, created_at) VALUES (10, '2025-10-06', 'Maulid Nabi Muhammad SAW', '2025-05-12 09:26:16');
INSERT INTO national_holidays (id, date, name, created_at) VALUES (11, '2025-12-25', 'Hari Natal', '2025-05-12 09:26:16');

-- Data for table rooms
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (69, 'ANT-Sta-3', 1, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (70, 'ANT-Sta-4', 1, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (71, 'ANT-Sta-5', 1, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (72, 'ANT-Sta-6', 1, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (73, 'ANT-Sta-7', 1, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (74, 'ANT-Sta-8', 1, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (75, 'ANT-Sta-9', 1, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (76, 'ANT-Sta-10', 1, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (77, 'ANT-Sta-11', 1, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (78, 'ANT-Eks-1', 1, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (79, 'ANT-Eks-2', 1, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (80, 'ANT-Eks-3', 1, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (81, 'ANT-Eks-4', 1, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (82, 'ANT-Eks-5', 1, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (83, 'ANT-Eks-6', 1, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (84, 'ANT-Eks-7', 1, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (85, 'ANT-Eks-8', 1, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (86, 'ANT-Eks-9', 1, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (87, 'ANT-Eks-10', 1, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (88, 'GUR-Sta-1', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (89, 'GUR-Sta-2', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (90, 'GUR-Sta-3', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (91, 'GUR-Sta-4', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (92, 'GUR-Sta-5', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (93, 'GUR-Sta-6', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (94, 'GUR-Sta-7', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (95, 'GUR-Sta-8', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (96, 'GUR-Sta-9', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (97, 'GUR-Sta-10', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (98, 'GUR-Sta-11', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (99, 'GUR-Sta-12', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (100, 'GUR-Sta-13', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (101, 'GUR-Sta-14', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (102, 'GUR-Sta-15', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (103, 'GUR-Sta-16', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (104, 'GUR-Sta-17', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (105, 'GUR-Sta-18', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (106, 'GUR-Sta-19', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (107, 'GUR-Sta-20', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (108, 'GUR-Sta-21', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (109, 'GUR-Sta-22', 2, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (110, 'GUR-Eks-1', 2, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (111, 'GUR-Eks-2', 2, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (112, 'GUR-Eks-3', 2, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (113, 'GUR-Eks-4', 2, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (114, 'GUR-Eks-5', 2, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (115, 'GUR-Eks-6', 2, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (116, 'GUR-Eks-7', 2, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (117, 'GUR-Eks-8', 2, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (118, 'GUR-Eks-9', 2, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (119, 'GUR-Eks-10', 2, 'Eksekutif', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (121, 'PES-Sta-2', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (122, 'PES-Sta-3', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (123, 'PES-Sta-4', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (124, 'PES-Sta-5', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (125, 'PES-Sta-6', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (126, 'PES-Sta-7', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (127, 'PES-Sta-8', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (128, 'PES-Sta-9', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (129, 'PES-Sta-10', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (130, 'PES-Sta-11', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (131, 'PES-Sta-12', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (132, 'PES-Sta-13', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (133, 'PES-Sta-14', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (134, 'PES-Sta-15', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (135, 'PES-Sta-16', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (136, 'PES-Sta-17', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (137, 'PES-Sta-18', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (138, 'PES-Sta-19', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (139, 'PES-Sta-20', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (140, 'PES-Sta-21', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (141, 'PES-Sta-22', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (142, 'PES-Sta-23', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (143, 'PES-Sta-24', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (144, 'PES-Sta-25', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (145, 'PES-Sta-26', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (146, 'PES-Sta-27', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (147, 'PES-Sta-28', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (148, 'PES-Sta-29', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (149, 'PES-Sta-30', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (150, 'PES-Sta-31', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (151, 'PES-Sta-32', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (152, 'PES-Sta-33', 3, 'Standard', 0, 'available', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (67, 'ANT-Sta-1', 1, 'Standard', 3100000, 'occupied', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (68, 'ANT-Sta-2', 1, 'Standard', 1550000, 'occupied', '2025-05-12 10:05:03');
INSERT INTO rooms (id, number, property_id, room_type, monthly_rate, status, created_at) VALUES (120, 'PES-Sta-1', 3, 'Standard', 1200000, 'occupied', '2025-05-12 10:05:03');

-- Data for table financial_records
INSERT INTO financial_records (id, property_id, transaction_date, amount, transaction_type, category, description, created_at, created_by) VALUES (1, 1, '2025-05-12', 6200000, 'income', 'Sewa', 'Pembayaran sewa oleh agus untuk 2 bulan (occupancy_id=2)', '2025-05-12 12:11:35', 1);
INSERT INTO financial_records (id, property_id, transaction_date, amount, transaction_type, category, description, created_at, created_by) VALUES (2, 1, '2025-05-12', 3100000, 'income', 'Sewa', 'Pembayaran sewa oleh agus untuk 2 bulan (occupancy_id=3)', '2025-05-12 12:11:35', 1);
INSERT INTO financial_records (id, property_id, transaction_date, amount, transaction_type, category, description, created_at, created_by) VALUES (3, 3, '2025-05-12', 3600000, 'income', 'Sewa', 'Pembayaran sewa kamar PES-Sta-1 (Standard) oleh yuli untuk 3 bulan', '2025-05-12 21:15:19', 11);
INSERT INTO financial_records (id, property_id, transaction_date, amount, transaction_type, category, description, created_at, created_by) VALUES (4, 3, '2025-05-12', 600000, 'expense', 'Internet', 'dibayar menggunakan uang saya dulu nanti diganti ya', '2025-05-12 21:17:52', 11);
INSERT INTO financial_records (id, property_id, transaction_date, amount, transaction_type, category, description, created_at, created_by) VALUES (5, 3, '2025-05-12', 250000, 'income', 'Layanan Tambahan', 'sewa tempat parkir bu Yuli', '2025-05-12 21:19:38', 11);

-- Data for table occupancy_records
INSERT INTO occupancy_records (id, room_id, month, is_occupied, tenant_name, notes, created_at, created_by, payment_status, payment_date, payment_due_date, payment_months) VALUES (2, 67, '2025-05', 1, 'agus', '', '2025-05-12 11:55:16', 5, 'paid', NULL, '2025-07-22', 2);
INSERT INTO occupancy_records (id, room_id, month, is_occupied, tenant_name, notes, created_at, created_by, payment_status, payment_date, payment_due_date, payment_months) VALUES (3, 68, '2025-05', 1, 'agus', '', '2025-05-12 11:57:17', 5, 'paid', NULL, '2025-07-22', 2);
INSERT INTO occupancy_records (id, room_id, month, is_occupied, tenant_name, notes, created_at, created_by, payment_status, payment_date, payment_due_date, payment_months) VALUES (4, 120, '2025-05', 1, 'yuli', 'akan tinggal di karawang selama 3 bulan dan bekerja di Unsika', '2025-05-12 21:15:19', 11, 'paid', NULL, '2025-08-23', 3);

SET FOREIGN_KEY_CHECKS=1;
