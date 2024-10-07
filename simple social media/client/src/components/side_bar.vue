<template>
    <aside class="bd-sidebar">
        <div class="offcanvas-lg offcanvas-start" tabindex="-1" id="offcanvas" aria-labelledby="offcanvasLabel">
            <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvasLabel">Offcanvas</h5>
                <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body">
                <nav class="bd-links w-100" id="bd-docs-nav" aria-label="Documents">
                    <strong class="bd-links-heading d-flex w-100 align-items-center fw-semibold fs-5">
                        Category
                    </strong>
                    <ul class="nav nav-pills flex-column">
                        <li class="nav-item">
                            <router-link :to="'/list/0'" class="nav-link" :class="{ active: $route.path === '/list/0'}">
                                All
                            </router-link>
                            <router-link :to="'/list/1'" class="nav-link" :class="{ active: $route.path === '/list/1'}">
                                Humor
                            </router-link>
                            <router-link :to="'/list/2'" class="nav-link" :class="{ active: $route.path === '/list/2'}">
                                Technology
                            </router-link>
                            <router-link :to="'/list/3'" class="nav-link" :class="{ active: $route.path === '/list/3'}">
                                Movies & TV
                            </router-link>
                            <router-link :to="'/list/4'" class="nav-link" :class="{ active: $route.path === '/list/4'}">
                                Video Games
                            </router-link>
                            <router-link :to="'/list/5'" class="nav-link" :class="{ active: $route.path === '/list/5'}">
                                Fashion
                            </router-link>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </aside>
</template>