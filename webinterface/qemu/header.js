document.write(`<section class="hero is-warning is-bold">
		<!-- this is the hero element head -->
		<div class="hero-head">
			<nav class="navbar is-fixed-top is-transparent">
				<div class="container">
					<div class="navbar-brand">
						<a class="navbar-item">
							<h1 class="title is-size-3 has-text-white">INSFP</h1>
						</a>
					</div>
					<div id="navbarMenuHeroA" class="navbar-menu">
						<div class="navbar-end">
            <div class="navbar-brand">

                    <span class="navbar-item">
											<a href="../docker/create_ctr_form.html"
												class="button is-link is-rounded">
												<span class="icon">
													<i class="fab fa-docker"></i>
												</span>
												<span>Docker</span>
											</a>
										</span>

            </div>
							<div class="navbar-brand">
								<div class="navbar-item has-dropdown is-hoverable">
									<a class="navbar-link">
										Menu
									</a>
									<div class="navbar-dropdown is-boxed">
										<a href="http://192.168.122.3/index.html" class="navbar-item">
											Home
										</a>
										<a href="documentation.html" class="navbar-item">
											Docs
										</a>
										<a href="about.html" class="navbar-item">
											About
										</a>
										<hr class="navbar-devider is-warning">
										<span class="navbar-item">
											<a href="https://github.com/xradiation"
												class="button is-warning is-rounded is-inverted">
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
					Qemu/KVM
				</h1>
				<h2 class="subtitle">
					Virtualization Server
				</h2>
			</div>
		</div>
		<!-- this is the hero element footer -->
		<div class="hero-foot">
			<nav class="tabs is-boxed is-fullwidth">
				<div class="container">
					<ul>`);
if (document.title == "Create VM") {
								document.write(`<li class="is-active"><a href="create_vm_form.html">Create VM</a></li>
								<li><a href="start_vm_form.html">Start VM</a></li>
								<li><a href="downloads.html">Downloads</a></li>
								<li><a href="debugging.html">Qemu</a></li>`);
}	else if (document.title == "Start VM") {
								document.write(`<li><a href="create_vm_form.html">Create VM</a></li>
								<li class="is-active"><a href="start_vm_form.html">Start VM</a></li>
								<li><a href="downloads.html">Downloads</a></li>
								<li><a href="debugging.html">Qemu</a></li>`);
}	else if (document.title == "Downloads") {
								document.write(`<li><a href="create_vm_form.html">Create VM</a></li>
								<li><a href="start_vm_form.html">Start VM</a></li>
								<li class="is-active"><a href="downloads.html">Downloads</a></li>
								<li><a href="debugging.html">Qemu</a></li>`);
}	else if (document.title == "Qemu") {
								document.write(`<li><a href="create_vm_form.html">Create VM</a></li>
								<li><a href="start_vm_form.html">Start VM</a></li>
								<li><a href="downloads.html">Downloads</a></li>
								<li class="is-active"><a href="debugging.html">Qemu</a></li>`);
}	else if (document.title == "About") {
								document.write(`<li><a href="create_vm_form.html">Create VM</a></li>
								<li><a href="start_vm_form.html">Start VM</a></li>
								<li><a href="downloads.html">Downloads</a></li>
								<li><a href="debugging.html">Qemu</a></li>`);
}
document.write(`					</ul>
				</div>
	</section>`);
