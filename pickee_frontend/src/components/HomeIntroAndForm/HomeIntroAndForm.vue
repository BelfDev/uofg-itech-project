<template>
    <div class="home-intro-and-form">
        <div class="page-home-screen page-home-screen--1" :class="{ 'page-home-screen--active': !isFormActive }">
            <div class="page-home-content">
                <PageHeader />
                <Intro :change-screen-method="showFormScreen" />
            </div>
            <div class="page-home-content-bg"></div>
            <div class="stripe stripe--light"></div>
            <div class="stripe stripe--lighter"></div>
            <div class="stripe stripe--dark"></div>
        </div>
        <div class="page-home-screen page-home-screen--2" :class="{ 'page-home-screen--active': isFormActive }">
            <div class="page-home-content">
                <PageHeader />
                <CasualPreferencesSelection />
            </div>
            <div class="stripe stripe--alt stripe--light"></div>
            <div class="stripe stripe--alt stripe--lighter"></div>
        </div>
    </div>
</template>

<script src="./HomeIntroAndForm.js" />
<style src="./HomeIntroAndForm.css" />