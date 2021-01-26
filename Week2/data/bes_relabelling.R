library("FactoRMine")
library("haven")
library("plyr")
library("dplyr")

options(
  summary.stats.lm = c(
    "R-squared",
    "p",
    "Deviance",
    "AIC",
    "BIC"
  )
)

data <- read_stata("/home/lunayneko/Documents/Teaching/dpir-intro-python/Week2/data/bes_f2f_2017_v1.3.dta")

#' B: RESPONDENT'S ELECTORAL BEHAVIOUR
#'
#' B1: Did you vote in 2017?
#' B2: Who did you vote for?
#' B4: If you had voted, who would you have voted for?
#' ^^ The above two can likely be combined to a single preferred party variable.
#' B6: Why did you vote the way you did?
#' ^^ Answers (3, 4) indicate strategic voting, B6a checks actual preferred
#'    party.
#' B12-B13: How closely do Tories(12)/Labour(13) look after the interests of:
#'          - BAME
#'          - Trade unions
#'          - Middle class people
#'          - Big business
#'          - Working class people
#'          - People who are unemployed or on benefits
#'    1: Very closely<>Not at all closely :4
#'
#' C: ATTITUDES TOWARD VOTING
#'
#' C1: How interested were you in the general election? (1 very)
#' C2_2: _It is every citizen's duty to vote in an election_ (1 strong disagree)
#'
#' D: PARTY ID
#'
#' D1: Which party do you think of yourself as?
#' -> If no, D2: do you think of yourelf as a little closer to one?
#'    ->  If yes, D3: which party is that?
#' D4: Strength of party identification. Can add option (4) based on non-
#'     identifaction based on answer to D1/D2
#'
#' E: LEFT-RIGHT
#'
#' E1: Left-Right self-placement
#' ^^ Would be interesting to compare correlation of PCA with LR
#'
#' F1: Range of political statements:
#'  01 Ordinary working people get their fair share of the nation's wealth
#'  02 There is one law for the rich and one for the poor
#'  03 Young people today don't have enough respect for traditional British
#'     values
#'  04 Censorship of films and magazines is necessary to uphold moral standards
#'  05 There is no need for strong trade unions to protect
#'     employees' working conditions and wages
#'  06 Private enterprise is the best way to solve Britain's economic problems
#'  07 Major public services and industries ought to be in state ownership
#'  08 It is the government's responsibility to provide a job for everyone who
#'     wants one
#'  09 People should be allowed to organise public meetings to protest against
#'     the government
#'  10 People in Britain should be more tolerant of those who lead
#'    unconventional lives
#'  11 For some crimes, the death penalty is the most appropriate sentence
#'  12 People who break the law should be given stiffer sentences
#'
#' P: Europe 0-10, self and parties
#'
#' P1: How did you vote in the Brexit referendum?
#' P2: How would you have voted in the Brexit referendum?
#' P3_1: Own view, European integration
#'
#'
#' W: CLASS
#'
#' W1: Class self-identification (1 middle, 2 working, 3 other)
#' -> If not W1(1, 2), W2: if you had to choose, middle or working (upper is
#'                         option but not mentioned).
#'
#' Y: DEMOGRAPHICS
#'
#' Y09: Gender
#' Y13A: Highest education achieved
#'
# Let's predict Brexit vote and whether they voted Tory.

vars <- c(
  "b01", "b02",
  "c01", "c02_2",
  "d01", "d03", "d02", "d04",
  "e01",
  "f01_1", "f01_2", "f01_3", "f01_4", "f01_5",
  "f01_6", "f01_7", "f01_8", "f01_9", "f01_10",
  "f01_11", "f01_12",
  "p01", "p02", "p03_1",
  "w01", "w02",
  "y09", "edlevel", "region")

df <- data %>% select(vars)

# Construct variables that are split over columns

f_batt <- c(
  "f01_1", "f01_2", "f01_3", "f01_4", "f01_5",
  "f01_6", "f01_7", "f01_8", "f01_9", "f01_10",
  "f01_11", "f01_12")
f_pca <- PCA(select(df, all_of(f_batt)), ncp=2)


df <- df %>% transmute(
  voted = factor(as.integer(b01==1), levels=c(0,1)),
  tory_vote = factor(tidyr::replace_na(b02==2, 0), levels=c(0,1)),
#  lab_vote = factor(replace_na(b02==1, 0), levels=c(0,1)),
  election_interest = as.integer(c01),
  civic_duty = as.integer(ifelse(c02_2==-1, 3, c02_2)),
  party_id = select(df, c("d01", "d03")) %>%
    apply(function(x){ifelse(x[1]<=0 & !is.na(x[2]),x[2],x[1])}, MARGIN=1) %>%
    mapvalues(attr(data$d01, 'labels'), labels(attr(data$d01, 'labels'))) %>%
    factor(),
  ideo_lr = as.integer(ifelse(df$e01<0, 5, df$e01)),
  ideo_pc1 = f_pca$ind$coord[,"Dim.1"],
  ideo_pc2 = f_pca$ind$coord[,"Dim.2"],
  vote_leave = factor(as.integer(p01==2)),
  class = factor(ifelse(df$w01!=1&df$w01!=2, df$w02, df$w01)),
  female = factor(as.integer(y09==2)),
  edlevel = factor(tidyr::replace_na(edlevel, 0)),
  region = factor(region) %>% relevel(ref="London")
)

feather::write_feather("bes_data.feather")
write.csv("bes_data.csv")

