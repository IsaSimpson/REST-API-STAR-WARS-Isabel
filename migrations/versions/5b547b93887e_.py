"""empty message

Revision ID: 5b547b93887e
Revises: 180047489a17
Create Date: 2024-07-28 11:38:20.113252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b547b93887e'
down_revision = '180047489a17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('height', sa.String(length=64), nullable=True),
    sa.Column('mass', sa.String(length=64), nullable=True),
    sa.Column('hair_color', sa.String(length=64), nullable=True),
    sa.Column('skin_color', sa.String(length=64), nullable=True),
    sa.Column('eye_color', sa.String(length=64), nullable=True),
    sa.Column('birth_year', sa.String(length=64), nullable=True),
    sa.Column('gender', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('diameter', sa.String(length=64), nullable=True),
    sa.Column('rotation_period', sa.String(length=64), nullable=True),
    sa.Column('orbital_period', sa.String(length=64), nullable=True),
    sa.Column('gravity', sa.String(length=64), nullable=True),
    sa.Column('population', sa.String(length=64), nullable=True),
    sa.Column('climate', sa.String(length=64), nullable=True),
    sa.Column('terrain', sa.String(length=64), nullable=True),
    sa.Column('surface_water', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=128), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=128),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('email',
               existing_type=sa.String(length=128),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('username')

    op.drop_table('favorite_planet')
    op.drop_table('favorite_people')
    op.drop_table('planet')
    op.drop_table('people')
    # ### end Alembic commands ###
