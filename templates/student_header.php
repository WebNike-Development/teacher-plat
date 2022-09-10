<!doctype html>
<html lang="en">

<head>

    <!-- Basic Page Needs
================================================== -->
    <title>Free Learning Website For Student</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">

    <!-- CSS
================================================== -->
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/colors/blue.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js">
    <link href="//cdn.jsdelivr.net/npm/@sweetalert2/theme-dark@4/dark.css" rel="stylesheet">
    <script src="//cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.js"></script>
</head>

<body>

    <!-- Wrapper -->
    <div id="wrapper">

        <!-- Header Container
================================================== -->
        <header id="header-container" class="fullwidth transparent">

            <!-- Header -->
            <div id="header">
                <div class="container">

                    <!-- Left Side Content -->
                    <div class="left-side">

                        <!-- Logo -->
                        <div id="logo">
                            <a href="home.php"><img src="images/learning_website_logo.png" alt=""></a>
                        </div>

                        <!-- Main Navigation -->
                        <nav id="navigation">
                            <ul id="responsive">

                                <li><a href="home.php" class="current">My Posts</a>
                                </li>

                                <li><a href="#">Finds Tutors</a>
                                    <ul class="dropdown-nav">

                                        <li><a href="all_tutors.php">All Tutors</a></li>
                                        <li><a href="all_tutors.php">Online Tutors</a></li>
                                        <li><a href="online_teacher.php">Home Tutors</a></li>

                                    </ul>
                                </li>

                                <li><a href="#">Wallet</a>
                                    <ul class="dropdown-nav">

                                        <li><a href="all_tutor_job.php">Coin Wallets</a></li>
                                        <li><a href="all_tutor_job.php">Buy Coins</a></li>
                                        <li><a href="online_tutor_job.php">Payments</a></li>
                                        <li><a href="home_tutor_job.php">Accounnt(Getting Paid)</a></li>
                                        <li><a href="home_tutor_job.php">Invite Friends For Coins</a></li>
                                        <li><a href="home_tutor_job.php">Refer Anyone To Get Coins</a></li>

                                    </ul>
                                </li>

                                <li><a href="student_reviews.php" class="current">Reviews</a>
                                </li>
                                <!-- 
								<li><a href="assignment_help.php">Assignment Help</a>
									
								</li> -->

                                <!-- <li><a href="#">Pages</a>
							<ul class="dropdown-nav">
								<li>
									<a href="#">Open Street Map</a>
									<ul class="dropdown-nav">
										<li><a href="jobs-list-layout-full-page-map-OpenStreetMap.php">Full Page List + Map</a></li>
										<li><a href="jobs-grid-layout-full-page-map-OpenStreetMap.php">Full Page Grid + Map</a></li>
										<li><a href="single-job-page-OpenStreetMap.php">Job Page</a></li>
										<li><a href="single-company-profile-OpenStreetMap.php">Company Profile</a></li>
										<li><a href="pages-contact-OpenStreetMap.php">Contact</a></li>
										<li><a href="jobs-list-layout-1-OpenStreetMap.php">Location Autocomplete</a></li>
									</ul>
								</li>
								<li><a href="pages-blog.php">Blog</a></li>
								<li><a href="pages-pricing-plans.php">Pricing Plans</a></li>
								<li><a href="pages-checkout-page.php">Checkout Page</a></li>
								<li><a href="pages-invoice-template.php">Invoice Template</a></li>
								<li><a href="pages-user-interface-elements.php">User Interface Elements</a></li>
								<li><a href="pages-icons-cheatsheet.php">Icons Cheatsheet</a></li>
								<li><a href="pages-login.php">Login & Register</a></li>
								<li><a href="pages-404.php">404 Page</a></li>
								<li><a href="pages-contact.php">Contact</a></li>
							</ul>
						</li> -->

                            </ul>
                        </nav>
                        <div class="clearfix"></div>
                        <!-- Main Navigation / End -->

                    </div>
                    <!-- Left Side Content / End -->


                    <!-- Right Side Content / End -->
                    <div class="right-side">
                        <div class="header-widget hide-on-mobile">
                            <a href="request_tutor.php" class="log-in-button"><img class="crn" src="images/icon_crown.png"> <span>Go Premium</span></a>
                        </div>
                        <!--  User Notifications -->
                        <div class="header-widget hide-on-mobile">

                            <!-- Notifications -->
                            <div class="header-notifications">

                                <!-- Trigger -->
                                <div class="header-notifications-trigger">
                                    <a href="#"><i class="icon-feather-bell"></i><span>4</span></a>
                                </div>

                                <!-- Dropdown -->
                                <div class="header-notifications-dropdown">

                                    <div class="header-notifications-headline">
                                        <h4>Notifications</h4>
                                        <button class="mark-as-read ripple-effect-dark" title="Mark all as read" data-tippy-placement="left">
                                            <i class="icon-feather-check-square"></i>
                                        </button>
                                    </div>

                                    <div class="header-notifications-content">
                                        <div class="header-notifications-scroll" data-simplebar>
                                            <ul>
                                                <!-- Notification -->
                                                <li class="notifications-not-read">
                                                    <a href="dashboard-manage-candidates.php">
                                                        <span class="notification-icon"><i class="icon-material-outline-group"></i></span>
                                                        <span class="notification-text">
                                                            <strong>Michael Shannah</strong> applied for a job <span class="color">Full Stack Software Engineer</span>
                                                        </span>
                                                    </a>
                                                </li>

                                                <!-- Notification -->
                                                <li>
                                                    <a href="dashboard-manage-bidders.php">
                                                        <span class="notification-icon"><i class=" icon-material-outline-gavel"></i></span>
                                                        <span class="notification-text">
                                                            <strong>Gilbert Allanis</strong> placed a bid on your <span class="color">iOS App Development</span> project
                                                        </span>
                                                    </a>
                                                </li>

                                                <!-- Notification -->
                                                <li>
                                                    <a href="dashboard-manage-jobs.php">
                                                        <span class="notification-icon"><i class="icon-material-outline-autorenew"></i></span>
                                                        <span class="notification-text">
                                                            Your job listing <span class="color">Full Stack PHP Developer</span> is expiring.
                                                        </span>
                                                    </a>
                                                </li>

                                                <!-- Notification -->
                                                <li>
                                                    <a href="dashboard-manage-candidates.php">
                                                        <span class="notification-icon"><i class="icon-material-outline-group"></i></span>
                                                        <span class="notification-text">
                                                            <strong>Sindy Forrest</strong> applied for a job <span class="color">Full Stack Software Engineer</span>
                                                        </span>
                                                    </a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>

                                </div>

                            </div>

                            <!-- Messages -->
                            <div class="header-notifications">
                                <div class="header-notifications-trigger">
                                    <a href="#"><i class="icon-feather-mail"></i><span>3</span></a>
                                </div>

                                <!-- Dropdown -->
                                <div class="header-notifications-dropdown">

                                    <div class="header-notifications-headline">
                                        <h4>Messages</h4>
                                        <button class="mark-as-read ripple-effect-dark" title="Mark all as read" data-tippy-placement="left">
                                            <i class="icon-feather-check-square"></i>
                                        </button>
                                    </div>

                                    <div class="header-notifications-content">
                                        <div class="header-notifications-scroll" data-simplebar>
                                            <ul>
                                                <!-- Notification -->
                                                <li class="notifications-not-read">
                                                    <a href="dashboard-messages.php">
                                                        <span class="notification-avatar status-online"><img src="images/user-avatar-small-03.jpg" alt=""></span>
                                                        <div class="notification-text">
                                                            <strong>David Peterson</strong>
                                                            <p class="notification-msg-text">Thanks for reaching out. I'm quite busy right now on many...</p>
                                                            <span class="color">4 hours ago</span>
                                                        </div>
                                                    </a>
                                                </li>

                                                <!-- Notification -->
                                                <li class="notifications-not-read">
                                                    <a href="dashboard-messages.php">
                                                        <span class="notification-avatar status-offline"><img src="images/user-avatar-small-02.jpg" alt=""></span>
                                                        <div class="notification-text">
                                                            <strong>Sindy Forest</strong>
                                                            <p class="notification-msg-text">Hi Tom! Hate to break it to you, but I'm actually on vacation until...</p>
                                                            <span class="color">Yesterday</span>
                                                        </div>
                                                    </a>
                                                </li>

                                                <!-- Notification -->
                                                <li class="notifications-not-read">
                                                    <a href="dashboard-messages.php">
                                                        <span class="notification-avatar status-online"><img src="images/user-avatar-placeholder.png" alt=""></span>
                                                        <div class="notification-text">
                                                            <strong>Marcin Kowalski</strong>
                                                            <p class="notification-msg-text">I received payment. Thanks for cooperation!</p>
                                                            <span class="color">Yesterday</span>
                                                        </div>
                                                    </a>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>

                                    <a href="dashboard-messages.php" class="header-notifications-button ripple-effect button-sliding-icon">View All Messages<i class="icon-material-outline-arrow-right-alt"></i></a>
                                </div>
                            </div>

                        </div>
                        <!--  User Notifications / End -->

                        <!-- User Menu -->
                        <div class="header-widget">

                            <!-- Messages -->
                            <div class="header-notifications user-menu">
                                <div class="header-notifications-trigger">
                                    <a href="#">
                                        <div class="user-avatar status-online"><img src="images/user.jpeg" alt=""></div>
                                    </a>
                                </div>

                                <!-- Dropdown -->
                                <div class="header-notifications-dropdown">

                                    <!-- User Status -->
                                    <div class="user-status">

                                        <!-- User Name / Avatar -->
                                        <div class="user-details">
                                            <div class="user-avatar status-online"><img src="images/user.jpeg" alt=""></div>
                                            <div class="user-name">
                                                Muhammad Qadama <span>Teacher</span>
                                            </div>
                                        </div>

                                        <!-- User Status Switcher -->
                                        <div class="status-switch" id="snackbar-user-status">
                                            <label class="user-online current-status">Online</label>
                                            <label class="user-invisible">Invisible</label>
                                            <!-- Status Indicator -->
                                            <span class="status-indicator" aria-hidden="true"></span>
                                        </div>
                                    </div>

                                    <ul class="user-menu-small-nav">
                                        <!-- <li><a href="dashboard.php"><i class="icon-material-outline-dashboard"></i> Dashboard</a></li> -->
                                        <li><a href="user_profile.php"><i class="icon-material-outline-settings"></i> Settings</a></li>
                                        <li><a href="index-logged-out.php"><i class="icon-material-outline-power-settings-new"></i> Logout</a></li>
                                    </ul>

                                </div>
                            </div>

                        </div>
                        <!-- User Menu / End -->

                        <!-- Mobile Navigation Button -->
                        <span class="mmenu-trigger">
                            <button class="hamburger hamburger--collapse" type="button">
                                <span class="hamburger-box">
                                    <span class="hamburger-inner"></span>
                                </span>
                            </button>
                        </span>

                    </div>
                    <!-- After Login Code Nabvbar  code -->
                    <!-- After Login Code Start -->

                    <!-- After Login Code End  -->
                    <!-- Right Side Content / End -->

                </div>
            </div>
            <!-- Header / End -->

        </header>
        <div class="clearfix"></div>
        <!-- Header Container / End -->