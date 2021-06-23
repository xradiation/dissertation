document.write(`<section class="hero is-link is-bold">
		<!-- this is the hero element head -->
		<div class="hero-head">
			<nav class="navbar is-fixed-top is-transparent">
				<div class="container">
					<div class="navbar-brand">
						<a class="navbar-item">
							<h1 class="title is-size-3 has-text-dark">INSFP</h1>
						</a>
					</div>
					<div id="navbarMenuHeroA" class="navbar-menu">
						<div class="navbar-end">
							<div class="navbar-brand">


                    <span class="navbar-item">
											<a href="../qemu/create_vm_form.html"
												class="button is-warning is-rounded">
												<span class="icon">
													<i class="far fa-object-ungroup"></i>
												</span>
												<span>&nbsp;Qemu&nbsp;</span>
											</a>
										</span>

								<div class="navbar-item has-dropdown is-hoverable">
									<a class="navbar-link">
										Menu
									</a>
									<div class="navbar-dropdown is-boxed">
										<a href="index.html" class="navbar-item">
											Home
										</a>
										<a href="documentation.html" class="navbar-item">
											Docs
										</a>
										<a href="about.html" class="navbar-item">
											About
										</a>
										<hr class="navbar-devider is-link">
										<span class="navbar-item">
											<a href="https://github.com/xradiation"
												class="button is-link is-rounded">
												<span class="icon">
													<i class="fab fa-github"></i>
												</span>
												<span>Project</span>
											</a>
										</span>
									</div>
								</div>
							</div>
						</div>
					</div>
			</nav>
		</div>
		<!-- this is the hero element body -->
		<div class="hero-body">
			<div class="container">
				<h1 class="title is-size-1">
					Docker
				</h1>
				<h2 class="subtitle">
					Containerization Server
				</h2>
			</div>
		</div>
		<!-- this is the hero element footer -->
		<div class="hero-foot">
			<nav class="tabs is-boxed is-fullwidth">
				<div class="container">
					<ul>`);
if (document.title == "Create Container") {
								document.write(`<li class="is-active"><a href="create_ctr_form.html">Create Container</a></li>
								<li><a href="start_ctr_form.html">Start Container</a></li>
								<li><a href="downloads.html">Downloads</a></li>
								<li><a href="debugging.html">Docker</a></li>`);
}	else if (document.title == "Start Container") {
								document.write(`<li><a href="create_ctr_form.html">Create Container</a></li>
								<li class="is-active"><a href="start_ctr_form.html">Start Container</a></li>
								<li><a href="downloads.html">Downloads</a></li>
								<li><a href="debugging.html">Docker</a></li>`);
}	else if (document.title == "Downloads") {
								document.write(`<li><a href="create_ctr_form.html">Create Container</a></li>
								<li><a href="start_ctr_form.html">Start Container</a></li>
								<li class="is-active"><a href="downloads.html">Downloads</a></li>
								<li><a href="debugging.html">Docker</a></li>`);
}	else if (document.title == "Docker") {
								document.write(`<li><a href="create_ctr_form.html">Create Container</a></li>
								<li><a href="start_ctr_form.html">Start Container</a></li>
								<li><a href="downloads.html">Downloads</a></li>
								<li class="is-active"><a href="debugging.html">Docker</a></li>`);
}	else if (document.title == "About") {
								document.write(`<li><a href="create_ctr_form.html">Create Container</a></li>
								<li><a href="start_ctr_form.html">Start Container</a></li>
								<li><a href="downloads.html">Downloads</a></li>
								<li><a href="debugging.html">Docker</a></li>`);
}
document.write(`					</ul>
				</div>
	</section>`);
