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
                        <p>MadStax is a team of developers established in 2019 at a Hackathon they
                           didn't finish. It consists of two top tier developers, a bridge engineering 
                           prodigy, and a man from England. Currently we have a number of successful
                           projects completed, including a Top Trumps game so perfect we were sued 
                           by CD Projekt Red for plagiarizing Gwent. We are currently working on
                           expanding Pickee for a global roll-out and hope to compete with the titans
                           of industry: Alphabet, Apple, Blockbuster, etc. While we are currently based
                           in Glasgow, we are expecting to open our Singapore offices by the end of next
                           week, followed by Sydney, Hong Kong, San Francisco, and Milton Keynes.
                        </p>
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
                    avatar: "https://cdn.vuetifyjs.com/images/john.jpg" // TODO: update

                },
                {
                    name: "Pedro B.",
                    role: "Software Engineer",
                    avatar: "https://cdn.vuetifyjs.com/images/john.jpg" // TODO: update

                },
                {
                    name: "Rhys S.",
                    role: "Software Engineer",
                    avatar: "https://cdn.vuetifyjs.com/images/john.jpg" // TODO: update

                },
                {
                    name: "Nathan S.",
                    role: "Software Engineer",
                    avatar: "https://cdn.vuetifyjs.com/images/john.jpg" // TODO: update

                }

            ]
        }),
        methods: {},
        components: { PageHeader, PersonList }
    };
</script>
