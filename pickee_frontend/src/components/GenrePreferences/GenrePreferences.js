export default {
    name: "GenrePreferences",
    props: ['changeEvent'],
    data: () => ({
        select: ["Action"],
        items: ["Action", "Drama", "Fantasy", "Sci-Fi"],
    })
}