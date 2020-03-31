<template>
    <div class="home-intro-and-form">
        <div class="page-home-screen page-home-screen--1" :class="{ 'page-home-screen--active': !isFormActive }">
            <div class="page-home-content">
                <PageHeader :urls="urls" :user="data.user" />
                <Intro :change-screen-method="showFormScreen" />
            </div>
            <div class="page-home-content-bg"></div>
            <div class="stripe stripe--light"></div>
            <div class="stripe stripe--lighter"></div>
            <div class="stripe stripe--dark"></div>
        </div>
        <div class="page-home-screen page-home-screen--2" :class="{ 'page-home-screen--active': isFormActive, 'page-home-screen--hidden': isFormHidden }">
            <div class="page-home-content">
                <PageHeader :urls="urls" :user="data.user" />
                <CasualPreferencesSelection :urls="urls" :user="data.user" />
            </div>
            <div class="stripe stripe--alt stripe--light"></div>
            <div class="stripe stripe--alt stripe--lighter"></div>
        </div>
    </div>
</template>

<script src="./HomeIntroAndForm.js" />
<style src="./HomeIntroAndForm.css" />