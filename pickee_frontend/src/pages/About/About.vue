<template>
    <v-app>
        <div class="page-wrapper about-page">
            <PageHeader />
            <v-content class="page-content">
                <h1>We are<br /> <span class="heading1-accent">Pickee.</span></h1>
                <div class="about-page__content">
                    <PersonList :developers="developers"/>
                    <div class="about-page__text">
                        <h2>MadStax</h2>
                        <p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of “de Finibus Bonorum et Malorum” (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, “Lorem ipsum dolor sit amet..”, comes from a line in section 1.10.32.</p>
                    </div>
                </div>
            </v-content>
        </div>
    </v-app>
</template>

<script>
    import PageHeader from "@/components/PageHeader/PageHeader.vue";
    import PersonList from "@/components/PersonList/PersonList.vue";

    export default {
        name: "About",
        data: () => ({
            developers: [
                {
                    name: "Anton S.",
                    role: "Software Engineer",
                    avatar: "https://cdn.vuetifyjs.com/images/john.jpg"

                },
                {
                    name: "Pedro B.",
                    role: "Software Engineer",
                    avatar: "https://cdn.vuetifyjs.com/images/john.jpg"

                },
                {
                    name: "Rhys S.",
                    role: "Software Engineer",
                    avatar: "https://cdn.vuetifyjs.com/images/john.jpg"

                },
                {
                    name: "Nathan S.",
                    role: "Software Engineer",
                    avatar: "https://cdn.vuetifyjs.com/images/john.jpg"

                }

            ]
        }),
        methods: {},
        components: { PageHeader, PersonList }
    };
</script>


