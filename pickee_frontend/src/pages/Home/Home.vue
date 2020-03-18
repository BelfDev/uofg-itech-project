<template>
    <v-app>
        <div class="page-home">
            <v-content>
                <HomeIntroAndForm />
            </v-content>
        </div>
    </v-app>
</template>

<script>
    import HomeIntroAndForm from '@/components/HomeIntroAndForm/HomeIntroAndForm.vue';

    export default {
        name: "Home",
        data: () => ({}),
        methods: {},
        components: {
            HomeIntroAndForm
        }
    };
</script>
